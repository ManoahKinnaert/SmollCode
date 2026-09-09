"""
This file handles everything regarding settings.
"""

import pathlib, os
import json

SMOLL_SETTINGS_FOLDER = pathlib.Path.home() / ".smollcode"

class SettingsParser:

    BASIC_SETTINGS = {
        "version": "0.1 Beta",

        "providers": {
            "ollama": {
                "api url": "http://127.0.0.1:11434/v1/",
                "default models": {}
            },

            "openai": {
                "api url": "https://api.openai.com/v1/",
                "default models": {}
            },

            "anthropic": {
                "api url": "https://api.anthropic.com/v1/",
                "default models": {}
            }
        }
    }

    def __init__(self):
        self._file: str | None = str(SMOLL_SETTINGS_FOLDER / "settings.json")

    def get_version(self):
        return self._get("version")

    def get_current_default_model(self):
        return self._get("default")

    def get_current_default_model_details(self):
        default = self.get_current_default_model() 
        return self._get("providers")[default["provider"]]["models"][default["model"]]
    
    def get_default_model_providers(self):
        return self._get("providers").keys()

    def get_default_models(self, provider: str):
        if provider in self.get_default_model_providers():
            return self._get("providers")[provider]["models"]

    # basic get and set methods (for reading and writing settings)
    def _get(self, key: str):
        with open(self._file, "r") as file:
            return self._get_all()[key] 

    def _get_all(self):
        with open(self._file, "r") as file: return json.load(file)

    def _set(self, key: str, val: object):
        data = self._get_all()
        data[key] = val 
        with open(self._file, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def settings_exist(self):
        return os.path.exists(self._file)

    def generate_basic_settings(self):
        os.makedirs(SMOLL_SETTINGS_FOLDER)
        
        with open(self._file, "w") as file:
            json.dump(self.BASIC_SETTINGS, file, ensure_ascii=False, indent=4)
