from funcs import *

hotel = {
    'simple': 50,
    'deluxe': 100,
    'breakfast': 10,
    'OceanView': 15,
}

reservations = {}

user_count = 0

print("\n\tWelcome to our Hotel best in the town!!")
while True:
    choice = landing_messages()
    if choice == '1':
        make_reservation(hotel, reservations, count=user_count+1)
    if choice == '2':
        format_reservations(reservations)
    if choice == '3':
        cost_of_staying(reservations)
    if choice == '4':
        name = input('Give name to cansel res: ')
        cansel_res(reservations, name)
    if choice == '5':
        print('Bye Bye')
        break
    user_count += 1









