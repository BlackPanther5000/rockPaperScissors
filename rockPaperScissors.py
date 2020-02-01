'''
Created on Feb 1, 2020

@author: ITAUser
'''

keepPlaying = True

while keepPlaying == True:
    print("Welcome to Rock, Paper, Scissors!")
    print("The game will be be best two out of three. If you want to quit, press 'Q'.")
    
    from random import randint
    
    compScore = 0
    playerScore = 0
    
    while playerScore < 2 and compScore < 2:
        compChoice = randint(1,3)
        print("--------------------------------------------------------------------------")
        playerChoice = input("Rock, Paper, or Scissors? ")
        playerChoice = playerChoice.lower()

        if playerChoice == "rock":
            playerChoice = 1
        elif playerChoice == "paper":
            playerChoice = 2
        elif playerChoice == "scissors":
            playerChoice = 3

        if playerChoice == "q":
            keepPlaying = False
            print("--------------------------------------------------------------------------")
            print("You have quit the game.")
            break
        elif (playerChoice == 1 and compChoice == 1) or (playerChoice == 2 and compChoice == 2) or (playerChoice == 3 and compChoice == 3):
            if playerChoice == 1:
                print("You chose: Rock")
                print("The computer chose: Rock")
            elif playerChoice == 2:
                print("You chose: Paper")
                print("The computer chose: Paper")
            elif playerChoice == 3:
                print("You chose: Scissors")
                print("The computer chose: Scissors")
            print("Draw!")
            print("Your score is: " , playerScore)
            print("The computer's score is: " , compScore)
            
        elif (playerChoice == 1 and compChoice == 3) or (playerChoice == 2 and compChoice == 1) or (playerChoice == 3 and compChoice == 2):
            if playerChoice == 1:
                print("You chose: Rock")
                print("The computer chose: Scissors")
            elif playerChoice == 2:
                print("You chose: Paper")
                print("The computer chose: Rock")
            elif playerChoice == 3:
                print("You chose: Scissors")
                print("The computer chose: Paper")
            print("You win!")
            playerScore += 1
            print("Your score is: " , playerScore)
            print("The computer's score is: " , compScore)

        elif (playerChoice == 1 and compChoice == 2) or (playerChoice == 2 and compChoice == 3) or (playerChoice == 3 and compChoice == 1):
            if playerChoice == 1:
                print("You chose: Rock")
                print("The computer chose: Paper")
            elif playerChoice == 2:
                print("You chose: Paper")
                print("The computer chose: Scissors")
            elif playerChoice == 3:
                print("You chose: Scissors")
                print("The computer chose: Rock")
            print("You lose!")
            compScore += 1
            print("Your score is: " , playerScore)
            print("The computer's score is: " , compScore)

        else:
            print("Your input was not valid. Please try again.")
    
       
    if playerScore == 2:
        print("--------------------------------------------------------------------------") 
        print("You won the game! Nice job!")
        break
    elif compScore == 2:
        print("--------------------------------------------------------------------------") 
        print("You lost the game! Better luck next time!")
        break
    
print("Thank you for playing!")