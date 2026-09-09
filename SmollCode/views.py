from render import *
import sys, tty, termios

def title_display(version: str, model_provider: str=None, model: str=None):
    render_title_logo()
    render_separator()
    if model_provider is None and model is None:
        render_markdown(markdown=f"Version: ** {version} ** ")
    elif model_provider is not None and model is not None:
        render_markdown(markdown=f"Version: ** {version} ** | Provider: ** {model_provider} ** | Model: ** {model} **")
    render_separator()


def selector(title: str, options: list):
    # render the title
    render_markdown(markdown=title)
    for i, _ in enumerate(options): options[i] = f"({i}) {options[i]}"
    markdown = str(options).replace("[", "").replace("]", "").replace(",", "").replace("'", "")
    render_markdown(markdown=markdown)
    user_input(f"Choose Option (0 to {len(options) - 1})")

def get_api_key():
    return get_secure("Enter API key") 

def provider_selector(providers):
    selector(title="** Choose a provider: **", options=providers)

def model_selector(models):
    selector(title="** Choose a model: ", options=models)