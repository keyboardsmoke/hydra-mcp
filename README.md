# Hydra MCP

This project implements a Hydra MCP (Model Control Protocol) server that enables Claude to interact with various client functions through a REST API interface. The system consists of a central server that coordinates communication between multiple clients and exposes their functions to Claude through a standardized API.

## Project Structure

- `ipc_server.py`: The central FastAPI server that manages function registration and routing
- `ipc_api.py`: The Hydra MCP interface that exposes client functions to Claude
- `fake_client.py`: A sample client implementation for testing
- `fake_claude.py`: A test implementation of Claude's interface

## Features

- Centralized function registry for multiple clients
- REST API endpoints for function discovery and invocation
- Standardized communication protocol between clients and Claude
- Easy-to-use function registration system
- Automatic function discovery and documentation

## API Endpoints

### Server Endpoints

- `POST /register_functions`: Register new functions from a client
- `GET /get_functions`: Retrieve the list of all registered functions

### MCP Tools

- `get_endpoints()`: List all available endpoints
- `get_registered_functions(endpoint)`: Get functions available at a specific endpoint
- `call_function(endpoint, function_name, arguments)`: Call a specific function with arguments

## Usage

1. Start the central server:
```bash
python ipc_server.py
```

2. Register client functions:
```python
# Example client registration
functions = [
    {
        "name": "example_function",
        "description": "An example function",
        "parameters": {
            "param1": "string",
            "param2": "integer"
        }
    }
]

requests.post(
    f"http://localhost:{API_SERVER_PORT}/register_functions",
    json={
        "endpoint": "client1",
        "functions": functions
    }
)
```

3. Use the MCP interface to interact with functions:
```python
# Get available endpoints
endpoints = get_endpoints()

# Get functions for a specific endpoint
functions = get_registered_functions("localhost:1234")

# Call a function
result = call_function("localhost:1234", "example_function", {"param1": "value", "param2": 42})
```

## Configuration

The server runs on port 6565 by default. This can be modified by changing the `API_SERVER_PORT` constant in both `ipc_server.py` and `ipc_api.py`.

## Dependencies

- FastAPI
- uvicorn
- requests
- fastmcp

## Testing

The project includes sample implementations (`fake_client.py` and `fake_claude.py`) for testing the functionality. These can be used as reference implementations for creating new clients or testing the system.
