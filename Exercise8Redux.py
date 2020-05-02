from random import randint

roshambo = ["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors! or Roshambo")

#Enemy players choices defined  by using the imported functio nrandint.
def EnemyPlayer():
    rNumber = int(randint(0,2))
    rChoice = roshambo[rNumber]
    return rChoice

#Game rules and point calculation
class Roshambo():

    def __init__(self, rounds: int):
        self._currentLevel = 1
        self._yourPoints = 0
        self._enemyPoints = 0
        self._rounds = rounds

    def _show_round_winners(self, yourChoice: str):
        opponentChoice = EnemyPlayer()
        print(" \n Your opponent chose: {} \n You chose: {} \n".format(opponentChoice, yourChoice))
        #Showing the round winners
        if (yourChoice=="rock"and opponentChoice=="scissors") or (yourChoice=="paper"and opponentChoice=="rock") or (yourChoice=="scissors"and opponentChoice=="paper"):
            print("You win!")
            self._yourPoints += 1
        elif (yourChoice=="rock"and opponentChoice=="paper") or (yourChoice=="paper"and opponentChoice=="scissors") or (yourChoice=="scissors"and opponentChoice=="rock"):
            print("You lose!")
            self._enemyPoints += 1
        elif yourChoice == opponentChoice:
            print("Draw!")
            self._yourPoints += 1
            self._enemyPoints += 1
        self._currentLevel += 1

    def _get_users_choice(self) -> str:
        while True:
            yourChoice = str(input("Rock, paper, or scissors? ").lower())
            if not yourChoice.isalpha():
                print("This is not a string")
            elif yourChoice not in roshambo:
                print("This is not a choice")
            else:
                return yourChoice

    def _point_comparison_and_winner(self):
        #Point comparison and game winner
        print("\n Enemy Score: {} \n Your Score: {} \n".format(self._enemyPoints, self._yourPoints))
        if self._enemyPoints > self._yourPoints:
            print("You lost the game by {} point(s)".format(self._enemyPoints - self._yourPoints))
        elif self._yourPoints > self._enemyPoints:
            print("You won the game by {} point(s)".format(self._yourPoints - self._enemyPoints))
        elif self._yourPoints == self._enemyPoints:
            print("Nobody won this game!")

    def execute(self):
        while (self._currentLevel <= self._rounds):
            print("You are currently on round {} of {} \n".format(self._currentLevel, self._rounds))
            yourChoice = self._get_users_choice()
            self._show_round_winners(yourChoice)
            self._point_comparison_and_winner()


def main():
    #Game start and initial input that initiates the Roshambo() function.
    while True:
        try:
            while True:
                choices = int(input("How many rounds would you like to play? "))
                if choices < 1:
                    print("You have to play at least 1 round.")
                else:
                    break
            roshambo = Roshambo(choices)
            roshambo.execute()
            break
        except ValueError:
            print("That is not a value.")

if __name__ == '__main__':
    main()
