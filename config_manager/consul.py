# Copyright (C) 2020 EdGE Networks Private Limited - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential, no part of this file may be replicated in any form

import json
from consul import Consul


class ConsulConfig(Consul):
    def __init__(self, host, port, http_scheme):
        super().__init__(host, port, scheme=http_scheme)

    def put_config(self, key, value):

        try:
            create_config_data = self.kv.put(key, value)
        except (AttributeError, TypeError):
            print("Failed to create Consul configuration data.")
            create_config_data = None
        except ConnectionError:
            print("Failed to connect to Consul service.")
            create_config_data = None
        except BaseException:
            print("Failed to create Consul configuration data. Please check consul service connection.")
            create_config_data = None
        return create_config_data

    def get_config(self, key):
        try:
            index, data = self.kv.get(key, recurse=True)
            config_data = json.loads(data[0]['Value'].decode())
        except (AttributeError, TypeError):
            print("Failed to fetch Consul configuration data. Please check configuration data configured or not.")
            config_data = None
        except ConnectionError:
            print("Failed to connect to Consul service.")
            config_data = None
        except BaseException:
            print("Failed to fetch Consul configuration data. Please check consul service connection.")
            config_data = None
        return config_data

