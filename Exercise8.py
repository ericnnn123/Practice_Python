from random import randint

roshambo = ["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors! or Roshambo")

#Enemy players choices defined  by using the imported functio nrandint.
def EnemyPlayer():
    rNumber = int(randint(0,2))
    rChoice = roshambo[rNumber]
    return rChoice

#Game rules and point calculation
def Roshambo(n):
    currentLevel = 1
    yourPoints = 0
    enemyPoints = 0
    while (currentLevel <= n):
        print("You are currently on round {} of {} \n".format(currentLevel, choices))
        while True:
            yourChoice = str(input("Rock, paper, or scissors? ").lower())
            if not yourChoice.isalpha():
                print("This is not a string")
            elif yourChoice not in roshambo:
                print("This is not a choice")
            else:
                break

        opponentChoice = EnemyPlayer()
        print(" \n Your opponent chose: {} \n You chose: {} \n".format(opponentChoice, yourChoice))

        #Showing the round winners
        if (yourChoice=="rock"and opponentChoice=="scissors") or (yourChoice=="paper"and opponentChoice=="rock") or (yourChoice=="scissors"and opponentChoice=="paper"):
            print("You win!")
            yourPoints += 1
        elif (yourChoice=="rock"and opponentChoice=="paper") or (yourChoice=="paper"and opponentChoice=="scissors") or (yourChoice=="scissors"and opponentChoice=="rock"):
            print("You lose!")
            enemyPoints += 1
        elif yourChoice == opponentChoice:
            print("Draw!")
            yourPoints += 1
            enemyPoints += 1
        currentLevel += 1

    #Point comparison and game winner
    print("\n Enemy Score: {} \n Your Score: {} \n".format(enemyPoints, yourPoints))
    if enemyPoints > yourPoints:
        print("You lost the game by {} point(s)".format(enemyPoints - yourPoints))
    elif yourPoints > enemyPoints:
        print("You wont the game by {} point(s)".format(yourPoints - enemyPoints))
    elif yourPoints == enemyPoints:
        print("Nobody won this game!")

#Game start and initial input that initiates the Roshambo() function.
while True:
    try:
        while True:
            choices = int(input("How many rounds would you like to play? "))
            if choices < 1:
                print("You have to play at least 1 round.")
            else:
                break
        break

        Roshambo(choices)
    except ValueError:
        print("That is not a value.")
    except choices == 0:
        print("You have to play a minimum of 1 turn.")
