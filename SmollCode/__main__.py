from views import title_display, get_api_key
from tools import *
from settings import SettingsParser
import os 

def main():
    settings_parser = SettingsParser()
    if not settings_parser.settings_exist(): settings_parser.generate_basic_settings()  # first startup stuff
    # we go for the default model by default...
    # register api key
    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None: 
        API_KEY = get_api_key()
    title_display(version="0.1 Beta", model_provider="Ollama (local)", model="MyModel")

if __name__ == "__main__":
    main()