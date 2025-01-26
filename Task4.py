import json

data = {"name": "Alice", "age": 20, "grade": "A"}
json_data = json.dumps(data)
print("JSON Data:", json_data)

parsed_data = json.loads(json_data)
print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("Grade:", parsed_data["grade"])
