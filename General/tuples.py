#tuples είναι παρομοίηες με τις λίστες , άλλα 
#τα στοιχεία σε ένα tuple δεν μπορούν να αλλάξουν 
#είναι αμτεβλήτα και αντί για [] χρησιμοποίουν ()

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#error
#dimensions[0] = 250

#tuple με ένα στοιχείο
mt_1 = (3,)
print(mt_1)

print("Oiginal dimencions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("Modified dimensions")
for dimension in dimensions:
    print(dimension)

#4-13 page105
Boufe = ('croissant','eggs','omelete','cereal','sausage')
print("Breakfast is serving today: ")
for item in Boufe:
    print(item)

Boufe = ('croissant','eggs','omelete','cake','tost')
print("New menu today :")
for item in Boufe:
    print(item)
