"""
This file handles everything regarding settings.
"""

import pathlib
import json

SMOLL_SETTINGS_FOLDER = pathlib.Path.home() / ".smollcode"
SMOLL_GENERAL_SETTINGS_FILE = SMOLL_SETTINGS_FOLDER / "general.json"
SMOLL_DEFAULT_MODELS_FILE = SMOLL_SETTINGS_FOLDER / "default_models.json"

class SettingsParser:
    def __init__(self):
        self._file: str | None = None

    def get_version(self):
        self._file = str(SMOLL_GENERAL_SETTINGS_FILE)
        return self._get("version")

    def get_current_default_model(self):
        self._file = str(SMOLL_DEFAULT_MODELS_FILE)
        return self._get("default")

    def get_current_default_model_details(self):
        default = self.get_current_default_model() 
        return self._get("providers")[default["provider"]]["models"][default["model"]]
    
    def get_default_model_providers(self):
        self._file = str(SMOLL_DEFAULT_MODELS_FILE)
        return self._get("providers").keys()

    def get_default_models(self, provider: str):
        self._file = str(SMOLL_DEFAULT_MODELS_FILE)
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
