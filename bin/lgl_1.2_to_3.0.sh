#!/bin/bash
ROOT_URL="https://api.littlegreenlight.com/api-docs/json/api-docs.json"
DOCS_DEST_DIR="docs"
SWAGGER_DEST_DIR="api_defs/swagger_1.2"
OPENAPI_DEST_DIR="api_defs/openapi_3.0"
CLIENT_DEST_DIR="clients/lgl_openapi_3.0_client"

mkdir -p "$SWAGGER_DEST_DIR"
curl -s "$ROOT_URL" -o "$SWAGGER_DEST_DIR/api-docs.json"

cat "$SWAGGER_DEST_DIR/api-docs.json" | grep -o 'lgl_api/v1/[^"]*' | sed 's/{format}/json/' | sort -u | while read endpoint; do
  echo "Fetching $endpoint..."
  mkdir -p "$SWAGGER_DEST_DIR/$(dirname $endpoint)"
  curl -s "https://api.littlegreenlight.com/api-docs/json/$endpoint" -o "$SWAGGER_DEST_DIR/$endpoint"
done

# Optional: fix the references in api-docs.json to use relative paths
sed -i '' 's|/api-docs/json/||g' "$SWAGGER_DEST_DIR/api-docs.json"

npx @openapitools/openapi-generator-cli generate -i $SWAGGER_DEST_DIR/api-docs.json \
  -g openapi \
  -o $OPENAPI_DEST_DIR \
  --skip-validate-spec

python build/fix_openapi_schema.py $OPENAPI_DEST_DIR/openapi.json $OPENAPI_DEST_DIR/openapi.json

python build/insert_openapi_security.py $OPENAPI_DEST_DIR/openapi.json $OPENAPI_DEST_DIR/openapi.json

# Set input and output directories
INPUT_DIR=$OPENAPI_DEST_DIR

# Generate from the 3.0 spec
npx @openapitools/openapi-generator-cli \
  generate -i "$OPENAPI_DEST_DIR/openapi.json" \
  -g markdown \
  -o $DOCS_DEST_DIR

npx @openapitools/openapi-generator-cli \
  generate -i "$OPENAPI_DEST_DIR/openapi.json" \
  -g python \
  -o $CLIENT_DEST_DIR

python clients/lgl_openapi_3.0_client/setup.py sdist bdist_wheel