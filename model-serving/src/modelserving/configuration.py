import os
import yaml
import modelserving
from . import logger


_logger = logger.get_logger(__name__)


class Configuration:
    def __init__(self, user_config_path):
        default_config = self._load_configuration(os.path.dirname(modelserving.__file__) + "/default.yml")
        user_config = self._load_configuration(user_config_path) if user_config_path is not None else {}

        self._config = self._merge_configuration(user_config, default_config)

    @staticmethod
    def _load_configuration(config_file):
        try:
            with open(config_file, 'r') as stream:
                try:
                    return yaml.safe_load(stream)
                except yaml.YAMLError:
                    return {}
        except IOError:
            return {}

    def _merge_configuration(self, source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                self._merge_configuration(value, node)
            else:
                destination[key] = value

        return destination

    def get(self, config_key_path):
        keys = config_key_path.split(".")
        current_config_node = self._config
        for key in keys:
            if key not in current_config_node:
                _logger.warn("Could not find configuration property '" + config_key_path + "' at '" + key + "'")
                return None

            current_config_node = current_config_node[key]

        return current_config_node
