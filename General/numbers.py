
for value in range(1,5+1):
    print(f"{value}")

#range se list

numbers = list(range(1,9))
print(numbers)

#even numbers in a list because we increase +2
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)


digits = [1,2,3,4,5,6,7,8,9,10,11]

print(min(digits))
print(max(digits))
print(sum(digits))

#advanced list implement
squares2 = [value**2 for value in range(1,5)]
print(squares2)


#do alone 4.3 page97
#for value in range (1,21):
    #print(value)

MilList = [value for value in range(1,10000001)]
#print(MilList)
print(max(MilList))
print(min(MilList))
print(sum(MilList))

odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)

tripleNums = []
for value in range(1,31):
    if value%3==0:
        tripleNums.append(value)

print(tripleNums)
