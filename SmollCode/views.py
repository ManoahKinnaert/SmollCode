from render import *

def title_display(version: str, model_provider: str, model: str):
    render_title_logo()
    render_separator()
    render_markdown(markdown=f"Version: ** {version} ** | Provider: ** {model_provider} ** | Model: ** {model} **")
    render_separator()

def model_selector():
    pass 