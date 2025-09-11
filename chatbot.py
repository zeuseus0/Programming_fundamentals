# 1. Asks for the user's name and stores it in a variable.
user_name = input("Hello! What's your name? ")

# 2. Greets them using their name.
print(" i am chatbot_#1. Nice to meet you, {user_name}!")

# 3. Asks how they are feeling today.
feeling = input("How are you feeling today? ")

# 4. Responds differently if they say 'good' or 'bad'.
if feeling == 'good':
    print("That's great to hear, {user_name}!")
elif feeling == 'bad':
    print("I'm sorry to hear that, {user_name}. I hope things get better for you soon.")
else:
    print("Thanks for sharing, {user_name}!")
    
    end