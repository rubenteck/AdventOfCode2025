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


def divide_by_type(data):
    types = {}
    for item in data:
        if item['type'] not in types:
            types[item['type']] = []
        types[item['type']].append(item)
    return types


def compress_data(data):
    result = {}

    for item in data:
        if item['name'] not in result:
            result[item['name']]= 0
        result[item['name']]+= item['quantity']
    return result

def get_most_popular_item(data):
    for _type in data:
        new_data = compress_data(data[_type])

        popular_items = []
        max_quantity = 0
        for item in new_data:
            if new_data[item] == max_quantity:
                popular_items.append(item)
            elif new_data[item] > max_quantity:
                max_quantity = new_data[item]
                popular_items = [item]

        popular_items.sort()
        data[_type] = popular_items[0]
    return data
    


print(sort_by_type(data))
print(get_most_popular_item(divide_by_type(data)))
# {'Candy': 1785, 'Clothing': 1982, 'Toy': 1729}
# action figure
