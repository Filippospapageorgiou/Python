import random

lottery = [21 , 20 , 36 , 1 , 3 ,5 , 22 , 9 , 5 , 8 , 'a' , 'b' , 't' , 'e ', 'm']
winning_seq = random.sample(lottery , 4)
print(f"winning_seq is {winning_seq}")

count = 0 
my_ticket = []

while True:
    for i in range(4):
        lucky_char = random.choice(lottery)
        my_ticket.append(lucky_char)
    
    if my_ticket == winning_seq:
        break
    my_ticket = []
    count += 1

print(f"{my_ticket}")
print(f"{count}")

    
    



