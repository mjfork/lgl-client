import json
import sys

SECURITY = [
    {"BearerAuth": []},
    {"BasicAuth": []},
    {"ApiKeyQuery": []}
]

SECURITY_SCHEMES = {
    "BearerAuth": {
        "type": "http",
        "scheme": "bearer"
    },
    "BasicAuth": {
        "type": "http",
        "scheme": "basic"
    },
    "ApiKeyQuery": {
        "type": "apiKey",
        "in": "query",
        "name": "access_token"
    }
}

def insert_openapi_security(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    # Insert security at the root
    data["security"] = SECURITY

    # Insert securitySchemes under components
    if "components" not in data:
        data["components"] = {}
    data["components"]["securitySchemes"] = SECURITY_SCHEMES

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Inserted security and securitySchemes. Output saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python insert_openapi_security.py <input_file> <output_file>")
        sys.exit(1)

    insert_openapi_security(sys.argv[1], sys.argv[2]) 