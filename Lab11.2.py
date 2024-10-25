import json

filename = "database.json"

def add_record(data, new_record):
    data.append(new_record)
    with open(filename, "w") as file:
        json.dump(data, file, indent=3)

def get_records_by_criterion(data, criterion):
    return [record for record in data if criterion in record.values()]

try:
    with open(filename, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

new_records = [
    {"name": "Anna", "age": 22},
    {"name": "David", "age": 25},
    {"name": "Alina", "age": 30}
]

for record in new_records:
    add_record(data, record)

criterion = 30
records = get_records_by_criterion(data, criterion)
print(records)