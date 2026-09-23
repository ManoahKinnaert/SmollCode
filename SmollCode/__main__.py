"""
Main file...
"""

from SmollCode.views import title_display, get_api_key
from SmollCode.agentic import agentic_loop
from SmollCode.tools import *
from SmollCode.settings import SettingsParser
import os 

def main():
    settings_parser = SettingsParser()
    if not settings_parser.settings_exist(): settings_parser.generate_basic_settings()  # first startup stuff
    # we go for the default model by default...
    current = settings_parser.get_current_default_model()
    title_display(
        version="0.1 Beta", 
        model_provider=current["provider"], 
        model=current["model"]
    )
    # register api key
    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None:
        API_KEY = get_api_key(settings_parser.get_current_default_provider_url())
    
    agentic_loop(provider_url=settings_parser.get_current_default_provider_url(), model=settings_parser.get_current_default_model_name(), api_key=API_KEY, settings_parser=settings_parser)

if __name__ == "__main__":
    main()