import json
import sys

def fix_openapi_schema(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    # Format mappings from short strings to valid schema objects
    format_mapping = {
        "float": {"type": "number", "format": "float"},
        "double": {"type": "number", "format": "double"},
        "date": {"type": "string", "format": "date"},
        "datetime": {"type": "string", "format": "date-time"},
        "string": {"type": "string"},
        "integer": {"type": "integer"},
        "number": {"type": "number"},
        "boolean": {"type": "boolean"}
    }

    fixed_count = 0
    schemas = data.get("components", {}).get("schemas", {})

    for schema_name, schema in schemas.items():
        props = schema.get("properties")
        if not isinstance(props, dict):
            continue

        for prop_name, prop_def in list(props.items()):
            # Case 1: Simple string, e.g., "float"
            if isinstance(prop_def, str) and prop_def in format_mapping:
                print(f"Fixing {schema_name}.{prop_name} from simple string '{prop_def}'")
                props[prop_name] = format_mapping[prop_def]
                fixed_count += 1
            # Case 2: $ref to primitive schema, e.g. "#/components/schemas/double"
            elif isinstance(prop_def, dict) and "$ref" in prop_def:
                ref_path = prop_def["$ref"]
                if ref_path.startswith("#/components/schemas/"):
                    ref_type = ref_path.split("/")[-1]
                    if ref_type in format_mapping:
                        print(f"Replacing $ref in {schema_name}.{prop_name} → {ref_type}")
                        props[prop_name] = format_mapping[ref_type]
                        fixed_count += 1
        # Force api_version to string
        if "api_version" in props:
            if props["api_version"] != {"type": "string"}:
                print(f"Forcing {schema_name}.api_version to string type")
                props["api_version"] = {"type": "string"}

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Fixed {fixed_count} malformed schema properties. Output saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fix_openapi_schema.py <input_file> <output_file>")
        sys.exit(1)

    fix_openapi_schema(sys.argv[1], sys.argv[2])