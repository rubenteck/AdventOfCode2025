import json

def read_input(file_name):
    # Open and read the JSON file
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data['children'], data['stock']

def give_gifts(children, stock):
    print_stack = []
    for child in children:
        present = ''
        for wish in child['wishlist']:
            if stock[wish] > 0:
                stock[wish] -= 1
                present = wish
                break
        print_out = f"{child['name']} gets {present}"
        print(print_out)
        print_stack.append(print_out)
        


children, stock =read_input('wishlistMatcherInput.json')
print(give_gifts(children, stock))

