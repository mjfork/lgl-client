# lgl-client

This project provides a Python client library for interacting with the Little Green Light (LGL) API, generated from the official OpenAPI specification.

## Installation

After the client has been generated (see DEVELOPER.md), you can install it using pip:

```bash
pip install clients/lgl_openapi_3.0_client/dist/lgl_openapi_3_0_client-<version>.tar.gz
```
Replace `<version>` with the actual version number of the generated package.

## Usage

Here's a basic example of how to use the generated LGL API client in your Python project:

```python
from lgl_openapi_3_0_client import ApiClient, Configuration, DefaultApi

# Configure the client
configuration = Configuration(
    host="https://api.littlegreenlight.com/v1",
    api_key={"access_token": "YOUR_API_KEY"}
)

with ApiClient(configuration) as api_client:
    api_instance = DefaultApi(api_client)
    # Example: List constituents
    response = api_instance.list_constituents()
    print(response)
```

Refer to the generated documentation in the `docs/` directory for detailed usage and available endpoints.

## Documentation

- [API Reference (Markdown)](docs/)
- [Little Green Light API Documentation](https://api.littlegreenlight.com/api-docs/)

## Support

For issues with the generated client, please open an issue in this repository or consult the official LGL API documentation.
