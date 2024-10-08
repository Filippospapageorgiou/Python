
#Λεξικό για την αποθυκεuση μαθητών και χρονια σποθδών

students = {}

while True:
    print("\n1. Add a student")
    print("2. Update student year")
    print("3. Delete a student")
    print("4. Show all students")
    print("5. Search for a student")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    if choice == '1':
        name = input('Enter students name: ')
        year = input('Enter students year of study: ')
        students[name] = year
        print(f"Student {name} added succesffuly!")

    elif choice == '2':
        name = input("Enter the students name to update:")
        if name in students:
            year = input(f"Enter the new year of study for {name}")
            students[name] = year
            print(f"Year of study for {name} updated to {year}!")
        else:
            print(f"{name} not Found!")

    elif choice == '3':
        name = input("Enter the student's name to delete: ")
        if name in students:
            del students[name]  # Διαγραφή φοιτητή
            print(f"Student {name} deleted successfully!")
        else:
            print(f"Student {name} not found!")

    elif choice == '4':
        if students:
            print("\nList of students:")
            for name , year in students.items():
                print(f"Name : {name} , Year : {year}")


    elif choice == '5':
        name = input("Enter the student's name to search: ")
        if name in students:
            print(f"{name} is in year {students[name]}.")
        else:
            print(f"Student {name} not found!")

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")



for year in students.values():
    print(f"{year}")
