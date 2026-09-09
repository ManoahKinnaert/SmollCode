from tools import TOOLS
import urllib.request
import json

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
            if not optional: required.append(param_name)
        result.append(
            {
                "name": name,
                "description": description,
                "input_schema": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            }
        )
    return result

def call_api(history, prompt, api_url: str, api_key: str, model: str):
    request = urllib.request.Request(
        api_url,
        data=json.dumps(
            {
                "model": model,
                "max_tokens": 8192,
                "system": prompt,
                "messages": history,
                "tools": make_schema(),
            }
        ).encode(),
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {api_key}"})
        },
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read())
