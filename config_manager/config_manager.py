from abc import ABC, abstractmethod
from config_manager.consul import ConsulConfig
from config_manager.file_system import FileConfig


class ConfigHandler(ABC):

    @abstractmethod
    def get_config_data(self, key):
        raise NotImplementedError


class ConsulConfigManager(ConfigHandler):

    def __init__(self, host, port, consul_path, http_scheme):
        self.consul_config = ConsulConfig(host, port, http_scheme)
        self.consul_path = consul_path

    def get_config_data(self, key):
        config_data = self.consul_config.get_config("{}{}".format(self.consul_path, key))
        if config_data is None:
            return False
        else:
            return config_data


class FileConfigManager(ConfigHandler):

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_configs = FileConfig(file_path)

    def get_config_data(self, key):
        try:
            return self.file_configs.configs[key]
        except KeyError:
            return False
