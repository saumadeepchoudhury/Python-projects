#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

Computer_won = 0
Player_won = 0

def Chosen_Option():
    chosen_option = input("Choose Rock, Paper or Scissors: ")
    if chosen_option in ["Rock", "rock", "R", "r"]:
        chosen_option = "r"
    elif chosen_option in ["Paper", "paper", "P", "p"]:
        chosen_option = "p"
    elif chosen_option in ["Scissors", "scissors", "S", "s"]:
        chosen_option = "s"
    else:
        print("Not a valid input, please try again.")
    return chosen_option

def Computer_Choice():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "r"
    elif computer_choice == 2:
        computer_choice = "p"
    else:
        computer_choice = "s"
    return computer_choice


while True:
    print("")
    
    chosen_option = Chosen_Option()
    computer_choice = Computer_Choice()

    print("")
    
    if chosen_option == "r":
        if computer_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
        
        elif computer_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
            
        elif computer_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    elif chosen_option == "p":
        if computer_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1
        
        elif computer_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")
            
            
        elif computer_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif chosen_option == "s":
        if computer_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
        
        elif computer_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1
            
        elif computer_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break


# In[ ]:





# In[ ]:




