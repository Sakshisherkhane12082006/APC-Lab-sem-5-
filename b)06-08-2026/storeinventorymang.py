inventory = {}

def add_product(name, quantity):
    inventory[name] = quantity

def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
    else:
        print("Product not found")

def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]

def highest_stock():
    product = max(inventory, key=inventory.get)
    print("Highest stock product:", product)
    print("Quantity:", inventory[product])

add_product("Pen", 50)
add_product("Book", 30)
add_product("Pencil", 70)

update_product("Book", 40)

inventory["Pen"] = 0
remove_product("Pen")

print("Inventory:", inventory)
highest_stock()
print("Total unique products:", len(inventory))