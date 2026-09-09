from render import *

def title_display(version: str, model_provider: str=None, model: str=None):
    render_title_logo()
    render_separator()
    if model_provider is None and model is None:
        render_markdown(markdown=f"Version: ** {version} ** ")
    elif model_provider is not None and model is not None:
        render_markdown(markdown=f"Version: ** {version} ** | Provider: ** {model_provider} ** | Model: ** {model} **")
    render_separator()

def model_selector():
    pass