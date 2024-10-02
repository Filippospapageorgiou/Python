
response = {}

polling_active = True
while polling_active:
    name = input("What is your name:")
    destination = input("What is your favroite mountain you want to visit plz answer:")

    response[name] = destination

    repeat = input("Want anyone else take the poll(yes,no):")
    if repeat == 'no':
        polling_active = False

print('\n-------Polling results-------')
for name , value in response.items():
    print(f"{name} - {value}")
