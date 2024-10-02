
promt = "if you tell me who you are , we can personalize the message you see"

promt += "\nWhat is your first name?"

name=input(promt)
print(f"hello {name}")

number = input("Enter a number , and i will tell you if it is odd")
number = int(number)

if number % 2 == 0:
    print("even")
else:
    print("odd")

promt = "Tell me something and i will repeat it back to you or 'quit' to exit: "

active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(f"{message}")