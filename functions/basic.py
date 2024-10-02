
menu = {
    'coffee' : 2.5,
    'tea' : 1.5,
    'sandwich' : 4.0,
    'cake' : 3.0,
}

orders = {}

def add_order(name , items):
    if name in orders:
        orders[name].extend(items)
    else:
        orders[name] = items
    print(f"Order add for {name}!")

def show_orders():
    print("\nOrders so far we have!!")
    if orders:
        for name , value in orders.items():
            print(f"{name}:{', '.join(value)}")
    else:
        print("No one has came yet :( ")

def calculate_total(name):
    if name in orders:
        total = 0
        for item in orders[name]:
            if item in menu:
                total += menu[item]
            else:
                print(f"Item {item} is not in the menu")
        return total
    else:
        print(f"No orders found for the name {name}")
        return None

def remove_order(name):
    if name in orders:
        del orders[name]
        print(f"Orders for {name} has been terminated")
    else:
        print(f"There is no orders for {name}")

add_order('John', ['coffee', 'sandwich'])
add_order('Anna', ['tea', 'cake'])
show_orders()

total_john = calculate_total('John')
if total_john:
    print(f"Total for John's order: ${total_john}")

remove_order('John')
show_orders()