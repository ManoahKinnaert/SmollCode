"""
This file handles everything regarding settings.
"""

import pathlib, os
import json

SMOLL_SETTINGS_FOLDER = pathlib.Path.home() / ".smollcode"

class SettingsParser:
    BASIC_SETTINGS = {
        "version": "0.1 Beta",

        "default model": {
            "provider": "ollama",
            "model": "qwen3"
        },

        "providers": {
            "ollama": {
                "api": "http://127.0.0.1:11434/v1",
                "models": {
                    "qwen3": {
                        "name": "qwen3.5:latest"
                    },

                    "llama3": {
                        "name": "llama3.2:3b"
                    }
                }
            },

            "anthropic": {
                "api": "https://api.anthropic.com/v1",
                "models": {}
            },
        }
    }

    def __init__(self):
        self._file: str | None = str(SMOLL_SETTINGS_FOLDER / "settings.json")

    def get_version(self):
        return self._get("version")

    def get_current_default_model(self):
        return self._get("default model")

    def get_current_default_provider_url(self):
        default_provider = self.get_current_default_model()["provider"]
        return self._get("providers")[default_provider]["api"]

    def get_provider_url(self, provider: str):
        return self._get("providers")[provider]["api"]

    def get_current_default_model_name(self):
        model = self.get_current_default_model()["model"]
        return self._get("providers")[self.get_current_default_model()["provider"]]["models"][model]["name"]

    def get_model_providers(self):
        return list(self._get("providers").keys())

    def get_models(self, provider: str):
        if provider in self.get_model_providers():
            return self._get("providers")[provider]["models"]

    def get_model_names(self, provider: str):
        return list(self.get_models(provider).keys())

    def get_model_name(self, provider: str, model: str):
        return self.get_models(provider)[model]["name"]

    def add_provider(self, name: str, api_url: str):
        self._set(key="providers", val={
            name: {
                "api url": api_url,
                "models": {}
            }
        })

    # TODO: To be implemented
    def add_model_to_provider(self, provider: str, model: str, details: str):
        pass 

    # TODO: To be implemented
    def remove_provider(self, name: str):
        pass 

    # basic get and set methods (for reading and writing settings)
    def _get(self, key: str):
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
