import json
import os


class LocalConfigLoader:
    def __init__(self):
        home_path = os.environ.get("SUSHI_HOME")
        self.config_path = home_path + "/config.json"
    def get_secret_config(self, key_name: str) -> dict:
        """

        :return: {'a_api_key': '***', 'b_api_key': '***'}
        """
        with open(self.config_path) as f:
            secrets = json.load(f).get("secrets")

        return secrets.get(key_name)
