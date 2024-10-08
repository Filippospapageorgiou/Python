

Students = []

while(True):
    print("1. Insert name in students List")
    print("2. Delete student from List")
    print("3. Show all students")
    print("4. Search for student")
    print("5. print number of students")
    print("6. Exit")

    
    choice = int(input("Choice:"))
    if choice == 1:
        name = input("Give name to add to list:")
        Students.append(name)
        print("Succes!")
    elif choice == 2:
        name = input("Give name to delete from list:")
        if name in Students:
            Students.remove(name)
        print("Succes")
    elif choice == 3:
        print("Students in list are:")
        for idx , student in emurate(Students):
            print(f"{idx+1}.{student}")
    elif choice == 4:
        print("Give mame to Search: ")
        name = input()
        if name in Students:
            print("Succes")
        else:
            print("Error didnt exist!")
    elif choice == 5:
        print(f"Number of Students: {len(Students)}.")
    elif choice == 6:
        print("Bye bye")
        break
    else:
        print("Wrong choose again!!")


