
def landing_messages():
    print('1. Create reservation')
    print('2. Show all reservations')
    print('3. Calculate cost of staying')
    print('4. Cansel Reservation by (name)')
    print('5. Exit..')
    choice = input("Request a service '1-5':")
    return choice

def make_reservation( hotel, reservations, count):
    print("Give your information for the one that creates the resrvation")
    firstname = input("firstname: ")
    lastname = input("lastname: ")

    print("Now select on of simple/deluxe rooms")
    print("And if you want any extra service")
    for item , value in hotel.items():
        print(f"{item} - {value}$")

    room = input("Give room 'simple or deluxe' : ")
    room = room.lower()
    while room != 'simple' and room != 'deluxe':
        room = input("Give room 'simple or deluxe' : ")

    breakfast = input("Breakfast while you are staying 'yes/no' ")
    breakfast = breakfast.lower()
    while breakfast != 'yes' and breakfast != 'no':
        breakfast = input("Breakfast while you are staying 'yes/no' ")

    if breakfast == 'yes':
        breakfast = True
    else:
        breakfast = False

    oceanview = input("OceanView while you are staying 'yes/no' ")
    oceanview = oceanview.lower()
    while oceanview != 'yes' and oceanview != 'no':
        oceanview = input("OceanView while you are staying 'yes/no' ")

    if oceanview == 'yes':
        oceanview = True
    else:
        oceanview = False

    days = input('How many days are you staying: ')


    userdata = {
        'firstname': firstname,
        'lastname': lastname,
        'room': room,
        'breakfast': breakfast,
        'ocean_view': oceanview,
        'days': days,
    }

    user = f"user{count}"
    reservations[user] = userdata


def format_reservations(reservations):
    print("\n All reservations in our system:\n")
    for data_user in reservations.values():
        print("------------------------------")
        for item, data in data_user.items():
            print(f"{item} - {data}")

    print("\nThat is all reservations!")


def cost_of_staying(reservations):
    print("\n Costs of staying of different clients:\n")

    for data_user in reservations.values():
        data = list(data_user.values())

        # Extract relevant data from the list
        room_type = data[2]  # Assuming room_type is the third element
        breakfast = data[3]  # Assuming breakfast is the fourth element
        ocean_view = data[4]  # Assuming ocean_view is the fifth element
        days = int(data[5])  # Assuming days is the sixth element (and converting to int)

        # Calculate the cost
        total = 0
        room_type = room_type.lower()

        if room_type == 'simple':
            total += 50
        elif room_type == 'deluxe':
            total += 100

        if breakfast:
            total += 15

        if ocean_view:
            total += 20

        total = total * days

        print(f"Cost of staying: {total}")

def cansel_res(reservations ,name):
    for user_key, data_user in list(reservations.items()):
        if data_user['firstname'] == name:
            del reservations[user_key]
            print(f"Reservation canceled for name : {name}")
            return
    print(f"No reservation found for name:{name}")



