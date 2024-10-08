
bisycles = ["trek","bmx","allon"]
print(bisycles)
print(bisycles[0])
print(bisycles[1].upper())

print(bisycles[-1]) # Η python στο -1 πάντα εμφανιζεί το τελυταιο στιχείο της λίστας

names = ["kostas","fabio","marios","giannis"]
print(names[0],names[1],names[2],names[-1])

message = f"Hy bro,{names[0].title()}"
print(message)

names[0] = message
print(names)

names.append("stelios")
names.insert(-1,"tasos")
print(names)

del names[1]
print(names)

popedName = names.pop() # mporoume na xrisimopoisoume kai pop(1) gia na afairesoume gia p.x to 2 stoixeio
print(popedName) # i pop mas dinei ti dianotita na xrisimopoisoume to stoixeio
print(names)

Geusts = ["Elon musk","Steve jobs","sydney sweene"]
geuestsMessage1 = f"Hy {Geusts[0].title()} you are invited to my party"
geuestsMessage2 = f"Hy {Geusts[1].title()} you are invited to my party"
geuestsMessage3 = f"Hy {Geusts[2].title()} you are invited to my party"
print(geuestsMessage1)
print(geuestsMessage2)
print(geuestsMessage3)

popGeusts = Geusts.pop(0)
print(f"{popGeusts.title()} can't come to the party")
print(Geusts)
