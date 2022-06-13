# This is a simple rock-paper-scissors game between the computer and the player.
# The possible options for the player to pick are: 
# "R" for "rock", 
# "P" for "paper", 
# "S" for "scissors"
# If the user inputs a value not among the options  it should print "invalid inpuit"
# If the value picked by the player == computer print "It's a tie" and restart the program
# If computer = R and player = S  print values picked + "You Lose" and ask if the player wants to play again, if yes restart the program , if not end the program
# if computer = P and player = R  print values picked + "You Lose" and ask if the player wants to play again, if yes restart the program, if not end the program 
# if computer = S and player = P  print values picked + "You Lose" and ask if the player wants to play again, if yes restart the program, if not end the program 

import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    player = input("rock, paper, scissors ? :").lower()

    while player not in choices:
        print("Invalid choice")

    if player == computer:
        print("computer=" ,computer, ":","player=" ,player )
        print("It's a tie")
    elif player == "rock":
        if computer =="paper":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU LOSE!")
        if computer =="scissors":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU WIN!")   
    elif player == "scissors":
        if computer =="rock":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU LOSE!")
        if computer =="paper":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU WIN!")           
    elif player == "paper":
        if computer =="scissors":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU LOSE!")
        if computer =="rock":
            print("computer=" ,computer, ":","player=" ,player )
            print("YOU WIN!")
            
    play_again = input("Play again? (Y/N):").lower()
    if play_again != "Y":
          break
print("Game Exited")
        
    