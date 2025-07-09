# LGL Client

A modular, type-safe Python client for the Little Green Light (LGL) REST API.

## Installation

```bash
pip install lgl-client
```

## Quick Start

```python
from lgl_client import new_client

# Initialize client with your API key
client = new_client("your-api-key")

# List categories
categories = client.categories.list()

# Get a specific constituent
constituent = client.constituents.get(123)
```

## Documentation

See the `dev/lgl_client/` directory for detailed API documentation.

## Security

Please read `SECURITY.md` for important security guidelines. 