inventory = {"item1": 3, "item2": 1, "item3": 5}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item in inventory:
        inventory[item] -= quantity
        
        if inventory[item] <= 0:
            del inventory[item]

add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

for key, value in inventory.items():
    print(f"{key}: {value}")