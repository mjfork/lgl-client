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

0. **(Optional) Clean the directories**
   ```bash
   bash bin/clean.sh
   ```
   This will remove all the directories with generated artifacts, allowing to start from a clean environment.


1. **Build the Python client package:**
   ```bash
   bash bin/lgl_1.2_to_3.0.sh
   ```
   This script will:
   - Download the LGL Swagger 1.2 API spec
   - Convert it to OpenAPI 3.0 format
   - Fix schema issues using `bin/fix_openapi_schema.py`
   - Inject security schemes using `bin/insert_openapi_security.py`
   - Generate Markdown documentation (`docs/`)
   - Generate the Python client library (`clients/lgl_openapi_3.0_client/`)
   - Generate the Python client package (`clients/lgl_openapi_3.0_client/dist/`)
   ```
   The distributable package will be available in `clients/lgl_openapi_3.0_client/dist/`.

## Project Structure

- `bin/lgl_1.2_to_3.0.sh`: Main automation script for the entire process.
- `bin/fix_openapi_schema.py`: Fixes malformed schema properties in OpenAPI specs.
- `bin/insert_openapi_security.py`: Injects security schemes into OpenAPI specs.
- `openapitools.json`: Configuration for OpenAPI Generator (if used).
- Output directories:
  - `api_defs/`: Downloaded and converted API definitions.
  - `docs/`: Generated Markdown documentation.
  - `clients/`: Generated Python client library.

## Customization

- Change OpenAPI Generator options in the shell script to generate clients in other languages or formats.