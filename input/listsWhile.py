
# move lists elements with while loop

uncofirmed_users = ['alice' , 'bob' , 'mat']
confirmed_users = []

while uncofirmed_users:
    current_user = uncofirmed_users.pop()

    print(f"Veryfiyng user {current_user.title()}")
    confirmed_users.append(current_user)

print("All confirmed users in my lost:")
for user in confirmed_users:
    print(f"Confirmed user : {user.title()}")