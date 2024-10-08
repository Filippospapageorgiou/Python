
cars = ["mercedes" , "bmw" , "audi" , "skoda"]
cars.sort()
print("sorting cars....")
print(cars)

#reversing sorting
cars.sort(reverse=True)
print(cars)

print("\nHere is the original list..")
print(cars)

print("Here is the sorted list:") #temperarly sorted
print(sorted(cars))

print("Original list again:",cars)

cars.reverse()
print(cars) # antistrofi listas

print(len(cars)) #mikos listas

#looping threw elements in a list

magicians = ["grey magic","oz","black"]
print("\n\nMagicians of metropolis..")
for magician in magicians:
    if magician == "oz":
        print("oz fuck off my stage")
        continue
    print(f"that was nice {magician}")


# 4.3 page 92 pizza ex 

pizzas = ["peperoni","bacon","chedar"]
print("\npizza proggram!!")
for pizza in pizzas:
    print(f"i like {pizza} pizza")

print(f"But i spesially love the {pizzas[1]} pizza more of all")
