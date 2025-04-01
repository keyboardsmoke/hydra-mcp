from typing import Any
from fastmcp import FastMCP
import requests

API_SERVER_PORT = 6565

mcp: FastMCP = FastMCP('ipc_api')

def call_endpoint(endpoint: str, function: str, arguments: dict[Any, Any]):
    """
    Call an endpoint with a function name and parameters
    """
    json_data = {
        "function": function,
        "arguments": arguments
    }
    url = f"http://{endpoint}/call_function"
    response = requests.post(url, json=json_data)
    return response.json()

def get_functions():
    """
    Get a list of endpoints and their functions from the MCP server
    """
    url = f"http://localhost:{API_SERVER_PORT}/get_functions"
    response = requests.get(url)
    return response.json()

@mcp.tool()
def get_endpoints():
    """
    Get a list of endpoints which can be used to get a list of functions
    The functions can then be called with the call_function tool
    """
    function_registry = get_functions()
    return list(function_registry.keys())

@mcp.tool()
def get_registered_functions(endpoint: str):
    """
    Get a list of registered functions
    """
    function_registry = get_functions()
    if endpoint not in function_registry:
        return {'status': 'error', 'message': f"endpoint {endpoint} not found"}
    return function_registry[endpoint]

@mcp.tool()
def call_function(endpoint: str, function_name: str, arguments: dict[Any, Any]):
    """
    Call a function with the given name and parameters
    """
    function_registry = get_functions()
    if endpoint not in function_registry:
        return {'status': 'error', 'message': f"endpoint {endpoint} not found"}
    
    for function in function_registry[endpoint]:
        if function["name"] == function_name:
            return call_endpoint(endpoint, function_name, arguments)
    return {'status': 'error', 'message': f"function {function_name} not found"}

def main():
    mcp.run()
    
main()
