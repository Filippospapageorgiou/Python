players = ['charles','martina','micael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

#slice se loop
print("Here are the 3 first players on my team:")
for player in players[:3]:
    print(player)

#copy lists

my_foods = ['pizza' , 'burger' , 'eggs']
friends_food = my_foods[:]

print("My fav food is:",my_foods)
print("My firends are this : ",friends_food)
