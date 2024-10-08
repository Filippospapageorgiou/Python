

alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_pos'] = 0 
alien_0['y_pos'] = 100
print(alien_0)


alien_0['color'] = 'yellow'
print(alien_0['color'])

del alien_0['points']
print(alien_0)

#del alien_0
#error because it deletes the var
# print(alien_0)

# get() use case

point_value = alien_0.get('points','no points asigned value exists')
print(point_value)

#6-1 page 139
dad = {
        'name'     : 'alex',
        'lastname' : 'papageorgiou',
        'age'      : 60,
        'town'     : 'korinth',
        }

print(f"Dad info {dad['name']} , {dad['lastname']} , {dad['age']} , {dad['town']} ")

#loop threw dic
for key , value in dad.items():
    print(key , value)
