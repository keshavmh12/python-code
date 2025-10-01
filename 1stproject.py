import random
user_choise = int(input("Please enter your choice:0 for rock,1 for paper,2 for scissor "))
computer_choice = random.randint(0,2)
if user_choise == computer_choice:
    print("Draw")
elif user_choise > computer_choice:
 print("You lose")
elif user_choise > computer_choice:
 print("You win")
elif computer_choice == 0 and user_choice == 2:
 print("You loss")
elif user_choise==0 and computer_choice==2:
   print("you win")




