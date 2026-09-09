from views import title_display, get_api_key, provider_selector
from render import user_input, error
from tools import *
import os 

def main():
    # register api key
    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None: 
        API_KEY = get_api_key()
    title_display(version="0.1 Beta", model_provider="Ollama (local)", model="MyModel")

    provider_selector(["One", "Two", "Three"])

if __name__ == "__main__":
    main()