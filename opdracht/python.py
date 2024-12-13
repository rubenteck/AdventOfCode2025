import json


# Open and read the JSON file
with open('santasToyInventoryInput.json', 'r') as file:
    data = json.load(file)

def sort_by_type(data):
    types = {}
    for item in data:
        if item['type'] not in types:
            types[item['type']] = 0
        types[item['type']] += item['quantity']
    return types

def get_most_popular_item(data):
    popular_items = []
    max_quantity = 0
    for item in data:

print(sort_by_type(data))

# {'Toy': 1729, 'Candy': 1785, 'Clothing': 1982}
