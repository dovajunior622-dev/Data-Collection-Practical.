import json

# Parse JSON string
data_string = '{"name": "Ayo", "age": 22}'
parsed = json.loads(data_string)

# Accessing the data
print(f"Parsed Name: {parsed['name']}")  # Output: Ayo
