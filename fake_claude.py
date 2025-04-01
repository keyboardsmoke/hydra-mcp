import requests

APP_PORT = 6577

# Just for testing purposes, this simulates a Claude call into the endpoint
def echo(message: str):
    json_data = {
        "function": "echo",
        "arguments": {
            "message": message
        }
    }
    res = requests.post(f"http://localhost:{APP_PORT}/call_function", json=json_data)
    print(res.json())

echo('Testing...')
