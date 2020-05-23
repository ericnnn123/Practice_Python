from random import randint

class GuessingNumberGame:
    def __init__(self):
        self.choices = ["up", "down", "correct", "quit"]
        self.turns = 1
        self.min = 0
        self.max = 10

    def validate_answer(self):
        while True:
            check_if_correct = input("Is this correct? ").lower()
            if check_if_correct not in self.choices:
                print("This is not an answer.")
            else:
                return check_if_correct
                break

    def evaluate_answer(self, answer):
        if answer == "up":
            self.min = self.guess_number
        elif answer == "down":
            self.max = self.guess_number

        print(self.min, self.max)

    def main_game(self):
        print("Your job is to think of a number between 1 and 10 and I'm going to guess it.\nOnly enter in 'up', 'down', or 'correct'. To exit out just type 'quit'. ")
        while True:
            self.guess_number = randint(self.min, self.max)
            print("My guess is: {}".format(self.guess_number))
            answer = self.validate_answer()

            if answer == "quit":
                print("Quitting the game...")
                break
            elif answer == "correct":
                print("Guessed the number in {} turns".format(self.turns))
                break
            else:
                self.evaluate_answer(answer)

            self.turns += 1

def main():
    game = GuessingNumberGame()
    game.main_game()

if __name__ == "__main__":
    main()
