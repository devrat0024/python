import random 

user_choice = int(input("Enter your choice: Type 0 for rock, Type 1 for paper, Type 2 for scissors: "))
computer_choice = random.randint(0, 2)

print("Computer's choice:", computer_choice)

if computer_choice == user_choice:
    print("It's a draw")
elif (computer_choice + 1) % 3 == user_choice:
    print("You win")
else:
    print("You lose")
