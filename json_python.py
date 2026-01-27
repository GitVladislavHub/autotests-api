import json

json_data = '{"name": "Ivan", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

data_2 = {
    "name": "Anoske",
    "age": 30,
    "is_student": False
}

json_data_2 = json.dumps(data_2, indent=4)

print(json_data_2, type(json_data_2))

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data, type(data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data_2, file, indent=4, ensure_ascii=False)
