# # Copyright (C) 2020 EdGE Networks Private Limited - All Rights Reserved
# # Unauthorized copying of this file, via any medium is strictly prohibited
# # Proprietary and confidential, no part of this file may be replicated in any form
#
from configparser import ConfigParser


class FileConfig:

    def __init__(self, file_path):
        config_parser = ConfigParser()
        config_parser.read(file_path)
        self.configs = {s: dict(config_parser.items(s, True)) for s in config_parser.sections()}
