#alien_0 = {'color':'green' , 'points':5}
#alien_1 = {'color':'yellow', 'points':10}
#alien_2 = {'color':'red',    'points':15}

#aliens = [alien_0 , alien_1 , alien_2]

#for alien in aliens:
    #print(alien)

aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#show the firs 5 aliens
for alien in aliens[:5]:
    print(alien)
print("....")


print(f"Total aliens created : {len(aliens)}")

#list inside dictianory

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # Fixed typo: 'musshrums' -> 'mushrooms'
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


##nesting dics in dics

users = {
        'ainstein':{
            'first':'albert',
            'last':'ainstein',
            'location':'prinston',
            },
        'mcurie':{
            'first':'marie',
            'last':'mcurie',
            'location':'paris',
            },
        }

for username , user_info in users.items():
    print(f"\nUsername: {username}")
    full_name=f"{user_info['first']}-{user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation:  {location.title()}")
    
