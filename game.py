import random
print('''The Computer: I chose a number from 1 to 100. Guess it!''')
print("Enter 'give up', if you can't guess it.")

computer_number = random.randint(1, 100)

user_choice = int(input("User:"))

while user_choice != "give up":

    if user_choice > computer_number:
        print("The Computer: Less!")
    elif user_choice < computer_number:
        print("The Computer: Grater!")
    else:
        print(f"The Computer: Congrats! You are lucky! The number really is : {computer_number}")
        break
    
    user_choice = int(input("User:"))
