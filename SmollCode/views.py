"""
Some helpful function for rendering certain views.
"""

from SmollCode.render import *
import urllib.request, urllib.error

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

def get_api_key(api_url: str):
    api_key = get_secure("Enter API key") 
    # we want to check if the api key is valid or not...
    request = urllib.request.Request(
        f"{api_url}/models",
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {api_key}"} if api_key else {})
        }
    )

    try:
        response = urllib.request.urlopen(request)
        if response.read() == 200:
            print("test")
    except urllib.error.HTTPError as e:
        print(e.read().decode())
        raise
    return api_key

def provider_selector(providers):
    return selector(title="** Choose a provider: **", options=providers)

def model_selector(models):
    return selector(title="** Choose a model: **", options=models)