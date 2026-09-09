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
    _options = options.copy()  # make copy
    for i, _ in enumerate(_options): _options[i] = f"({i}) {_options[i]}"
    markdown = str(_options).replace("[", "").replace("]", "").replace(",", "").replace("'", "")
    render_markdown(markdown=markdown)
    selected_option: str = user_input(f"Choose Option (0 to {len(_options) - 1})")
    # TODO: false input handling
    if not selected_option.isnumeric(): pass 
    return int(selected_option)

def get_api_key():
    return get_secure("Enter API key") 

def provider_selector(providers):
    return selector(title="** Choose a provider: **", options=providers)

def model_selector(models):
    return selector(title="** Choose a model: **", options=models)