import random 

user_choice =int(input("enter your choice:Type 0 for rock , Type 1 for paper , Type 2 for scissor : "))
computer_choice=random.randint(0,2)
print("computer_choice")
print(computer_choice)
if computer_choice == user_choice:
    print("It's a draw")
elif computer_choice > user_choice: #2>0
    print("you lose")
elif user_choice > computer_choice : #2>0
    print("you win")
elif computer_choice ==0 and user_choice ==2:  
    print("you lose")
elif user_choice ==0 and computer_choice ==2:
    print("you win") 