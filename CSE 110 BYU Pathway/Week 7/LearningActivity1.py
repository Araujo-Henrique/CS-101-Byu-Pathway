

def print_input_regular(users_message):
    message = users_message
    print(message)

def print_input_lowercase(user_message):
    message = user_message.lower()
    print(message)

def print_input_uppercase(user_message):
    message = user_message.upper()
    print(message)

users_message = input("What is your message? ")

print_input_regular(users_message)
print_input_lowercase(users_message)
print_input_uppercase(users_message)
