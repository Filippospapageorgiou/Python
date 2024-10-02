

sandwich_orders = ["hamm","butter","chesse"]
finished_sandwich = []

while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print(f"{current_sand} sandwich is ready..")

    finished_sandwich.append(current_sand)

print("All sandiches are ready..")


