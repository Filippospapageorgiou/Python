


def make_pizza(size,*toppings):
    print(f'\nMaking size {size} pizza with the following toppings:')
    for toping in toppings:
        print(f"-{toping}")

make_pizza(16,'masshrooms',)

make_pizza(12,'bacon','peper','pinaple')


def build_profile(firts,last , **user_info):
    user_info['first_name'] = firts
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('filippos','papageorgiou', uni = 'uniwa')
print(user_profile)