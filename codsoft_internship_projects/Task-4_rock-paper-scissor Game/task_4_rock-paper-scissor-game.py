import random

controls = ["rock" , "paper" , "scissors"]
play_again = True

print("---------------------------RULES-------------------------------\n")

print("1 _ rock BEATS scissors , scissors BEATS paper , paper BEATS rock \n")
print("2 _ The Winner is decided by compairing between the player's choice and computer's choice in which one beats another " \
"according to the above mentioned game rules.")
print("---------------------------RULES-------------------------------\n")

while play_again:
    
    player = None
    computer = random.choice(controls)

    while player not in controls:
        player = input("Enter your choice for game( rock, paper, scissors ) : ")
    


    print(f"\nThe player choice is : {player}")
    print(f"Computer choice : {computer}")

    if player == computer:
       print("\n---------------It is a Tie 'equal for both'------------")

    elif player == "rock" and computer == "scissors":
       print("\n----------------- you Win 🏆😁 ----------------")
    elif player == "scissors" and computer == "rock":
       print("\n---------------- you Lose 🤡😞 ----------------")

    elif player == "scissors" and computer == "paper":
       print("\n----------------- you Win 🏆😁 ----------------")
    elif player == "paper" and computer == "scissors":
       print("\n---------------- you Lose 🤡😞 ----------------")

    elif player == "paper" and computer == "rock":
       print("\n----------------- you Win 🏆😁 ----------------")
    elif player == "rock" and computer == "paper":
       print("\n---------------- you Lose 🤡😞 ----------------")

    if not input(" do you want to play again(y/n) ? :").lower() == "y": 
       play_again = False


print("GAME IS OVER , EXITED !")
print("\n")