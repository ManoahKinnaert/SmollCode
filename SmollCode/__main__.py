from views import title_display
from render import user_input
from tools import *

def main():
    title_display(version="0.1 Beta", model_provider="Ollama (local)", model="MyModel")
    user_input()

if __name__ == "__main__":
    main()