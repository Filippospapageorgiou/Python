

print("Welcome to the statistics game!!\n")

count = 0
total_sum = 0
numbers = []


print("pleaze give a numner or enter 'stop' to end the game.")

while(True):
    number = input(f"{count+1}.Number: ")

    if number.lower() == "stop":
        print("Stopping game!")
        break

    try:
        number = int(number)
        total_sum += number
        numbers.append(number)
        count += 1
    except ValueError:
        print(f"Invalid input pleaze enter a valid number or 'stop'.")
        continue

average = round(total_sum / count , 2)
if numbers:
    print("\nStatistics of the game:")
    print(f"Sum of numbers you gave : {total_sum}")
    print(f"Max number you gave     : {max(numbers)}")
    print(f"MIn number you gave     : {min(numbers)}")
    print(f"Average of nums         : {average}")
else:
    print("Empty list of numbers!")
