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
        if item['quantity'] == max_quantity:
            popular_items.append(item['name'])
        elif item['quantity'] > max_quantity:
            max_quantity = item['quantity']
            popular_items = [item['name']]

    popular_items.sort()
    return popular_items[0]


print(sort_by_type(data))
print(get_most_popular_item(data))
# {'Toy': 1729, 'Candy': 1785, 'Clothing': 1982}
