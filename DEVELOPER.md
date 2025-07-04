# Developer Guide: Generating the LGL API Client

This guide explains how to generate the Python client library and Markdown documentation for the Little Green Light (LGL) API from the official OpenAPI/Swagger specifications.

## Prerequisites

- **Python 3.x**
- **Node.js** (for OpenAPI Generator CLI)
- **@openapitools/openapi-generator-cli** (install globally or use npx)
- **Internet access** (to fetch LGL API specs)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Generation Steps

1. **Run the main automation script:**
   ```bash
   bash build/lgl_1.2_to_3.0.sh
   ```
   This script will:
   - Download the LGL Swagger 1.2 API spec
   - Convert it to OpenAPI 3.0 format
   - Fix schema issues using `build/fix_openapi_schema.py`
   - Inject security schemes using `build/insert_openapi_security.py`
   - Generate Markdown documentation (`docs/`)
   - Generate the Python client library (`clients/lgl_openapi_3.0_client/`)

2. **Build the Python client package:**
   ```bash
   python clients/lgl_openapi_3.0_client/setup.py sdist bdist_wheel
   ```
   The distributable package will be available in `clients/lgl_openapi_3.0_client/dist/`.

## Project Structure

- `build/lgl_1.2_to_3.0.sh`: Main automation script for the entire process.
- `build/fix_openapi_schema.py`: Fixes malformed schema properties in OpenAPI specs.
- `build/insert_openapi_security.py`: Injects security schemes into OpenAPI specs.
- `openapitools.json`: Configuration for OpenAPI Generator (if used).
- Output directories:
  - `api_defs/`: Downloaded and converted API definitions.
  - `docs/`: Generated Markdown documentation.
  - `clients/`: Generated Python client library.

## Customization

- Modify the Python scripts in `build/` to adjust schema fixes or security schemes as needed.
- Change OpenAPI Generator options in the shell script to generate clients in other languages or formats.

## Troubleshooting

- Ensure all prerequisites are installed and available in your PATH.
- If the OpenAPI Generator CLI is not found, install it globally with:
  ```bash
  npm install -g @openapitools/openapi-generator-cli
  ```
- For issues with the generated client, check the OpenAPI spec for errors or consult the OpenAPI Generator documentation. 