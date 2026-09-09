from views import title_display
from render import user_input, error, get_secure
from tools import *
import os 

def main():
    # register api key
    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None: 
        API_KEY = get_secure("Enter API key")
    title_display(version="0.1 Beta", model_provider="Ollama (local)", model="MyModel")
    user_input()

if __name__ == "__main__":
    main()