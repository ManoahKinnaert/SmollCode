"""
This file contains everything concerning agentic stuff, from api calls to function tool calling.
"""

from tools import TOOLS, execute_tool
from render import *
from views import provider_selector, model_selector
import urllib.request, urllib.error, json, os


def make_schema():
    result = []

    for name, (description, params, fn) in TOOLS.items():
        properties = {}
        required = []

        for param_name, param_type in params.items():
            optional = param_type.endswith("?")
            base_type = param_type.rstrip("?")

            properties[param_name] = {
                "type": "integer" if base_type == "number" else base_type
            }

            if not optional:
                required.append(param_name)

        result.append({
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        })

    return result


def call_api(history, prompt, api_url: str, api_key: str, model: str):
    request = urllib.request.Request(
        f"{api_url}/chat/completions",
        data=json.dumps({
            "model": model,
            "max_tokens": 8192,
            "messages": [
                {"role": "system", "content": prompt},
                *history,
            ],
            "tools": make_schema(),
        }).encode(),
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {api_key}"} if api_key else {}),
        },
    )

    try:
        response = urllib.request.urlopen(request)
        return json.loads(response.read())
    except urllib.error.HTTPError as e:
        print(e.read().decode())
        raise

# util function for computing tokens of chat
def compute_tokens(api_url: str, api_key: str, model: str, history):
    request = urllib.request.Request(
        f"{api_url}/repsonses/input_tokens",
        data=json.dumps({
            "model": model,
            "messages": history,

        }).encode(),
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {api_key}"} if api_key else {})
        }
    ) 

    try:
        response = urllib.request.urlopen(request)
        return json.loads(response.read())
    except urllib.error.HTTPError as e:
        if e.code == 404: yellow_message("It doesn't look like this API supports token compute at this time.")
        else: yellow_message(e.read().decode())
        return "Unknown"
        
def agentic_loop(provider_url: str, model: str, api_key: str, settings_parser):
    messages = []
    sys_prompt = f"Concise coding assistant, cwd: {os.getcwd()}"

    while True:
        try:
            user_in = user_input()

            if not user_in:
                continue

            if user_in.lower() in ("/q", "/exit", "/quit"):
                break

            if user_in.lower() == "/clear":
                messages = []
                green_message("Cleared conversation history!")
                continue

            if user_in.lower() == "/model":
                # select provider
                available_providers = settings_parser.get_model_providers()
                selected_provider = provider_selector(available_providers)
                selected_provider = available_providers[selected_provider]
                # select model
                available_models = settings_parser.get_model_names(selected_provider)
                selected_model = model_selector(available_models)
                model = settings_parser.get_model_name(provider=selected_provider, model=available_models[selected_model])
                provider_url = settings_parser.get_provider_url(selected_provider)
                # indicate that user has switched model
                render_markdown(f"Switched model | Provider: **{selected_provider}** | model: **{model}**")
                continue

            messages.append({
                "role": "user",
                "content": user_in,
            })

            while True:
                response = call_api(
                    history=messages,
                    prompt=sys_prompt,
                    api_url=provider_url,
                    api_key=api_key,
                    model=model,
                )

                message = response["choices"][0]["message"]
                messages.append(message)

                if message.get("content"):
                    render_markdown(message["content"])

                tool_calls = message.get("tool_calls", [])

                if not tool_calls:
                    break

                for tool_call in tool_calls:
                    tool_name = tool_call["function"]["name"]
                    tool_args = json.loads(
                        tool_call["function"]["arguments"]
                    )

                    arg_preview = (
                        str(list(tool_args.values())[0])[:50]
                        if tool_args else ""
                    )

                    indicate_tool_use(
                        tool_name=tool_name,
                        arg_preview=arg_preview,
                    )

                    result = execute_tool(tool_name, tool_args)

                    result_lines = result.split("\n")
                    preview = result_lines[0][:60]

                    if len(result_lines) > 1:
                        preview += f" ... +{len(result_lines) - 1} lines"
                    elif len(result_lines[0]) > 60:
                        preview += "..."

                    print(f"  {DIM}⎿  {preview}{RESET}")

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "content": result,
                    })

            print()
            render_markdown(f"Total used tokens: **{compute_tokens(provider_url, api_key, model, messages)}**")

        except (KeyboardInterrupt, EOFError):
            yellow_message("\nExiting...")
            exit(0)

        except Exception as err:
            error(err)