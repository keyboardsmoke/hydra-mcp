from typing import Any
from fastapi import FastAPI
import requests
import uvicorn

API_SERVER_PORT = 6565
APP_PORT = 6577

app = FastAPI()

def echo(message: str) -> None:
    print(message)

@app.post("/call_function")
async def call_function(data: dict[Any, Any]):
    function = data["function"]
    arguments = data["arguments"]
    if function == "echo":
        echo(**arguments)
        return {'status': 'success'}
    
    return {'status': 'error', 'message': f"Function {function} not found"}

def main():
    fn_json = {
        # Endpoint doesn't need protocol, ipc_api will use http://
        "endpoint": f"localhost:{APP_PORT}",
        "functions": [
            {
                "name": "echo", 
                "args": ["message: str"], 
                "return_type": "None", 
                "description": "Echo a message"
            }
        ]
    }
    
    print(fn_json)
    res = requests.post(f"http://localhost:{API_SERVER_PORT}/register_functions", json=fn_json)
    if res.status_code != 200:
        print(f"Failed to register functions: {res.json()}")
        return
    
    json_res = res.json()
    if json_res["status"] != "success":
        print(f"Unsuccessful registration: {json_res['message']}")
        return
    
    print(f"Successful registration: {json_res['message']}")
    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)

if __name__ == "__main__":
    main()

