from fastapi import FastAPI
import uvicorn

API_SERVER_PORT = 6565

app = FastAPI()

function_registry: dict[str, dict[str, dict]] = {}

@app.post("/register_functions")
async def register_functions(json_data: dict):
    """
    Register a list of functions with the MCP server
    """
    endpoint = json_data["endpoint"]
    functions = json_data["functions"]
    function_registry[endpoint] = functions
    return {'status': 'success', 'message': f"Received arguments"}

@app.get("/get_functions")
async def get_functions():
    """
    Get a list of endpoints and their functions from the MCP server
    """
    return function_registry

def main():
    uvicorn.run(app, host="0.0.0.0", port=API_SERVER_PORT)

main()
