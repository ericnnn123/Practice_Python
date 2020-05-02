from random import randint

class BullsandCows:
    def __init__(self):
        self.cows = 0
        self.bulls = 0
        self.user_guesses = 1

    def evaluate_user_input(self, question):
        while True:
            user_input = input(question)
            if user_input.isalpha():
                if user_input.lower() == "quit":
                    return False
                    break
                else:
                    print("You must enter a number that is bigger than 1000")

            elif user_input.isdigit():
                integer_input = int(user_input)
                if len(str(integer_input)) != 4:
                    print("You have to enter in a number with a length of 4.")
                else:
                    return integer_input
                    break
            else:
                print("Try entering in only numbers")

    def generate_checkable_number(self):
        random_number = randint(1000, 9999)
        checkable_number = []
        for index in str(random_number):
            checkable_number.append(int(index))
        print(checkable_number)
        return checkable_number

    def convert_user_input(self, user_input):
        checkable_user_number = []
        for index in str(user_input):
            checkable_user_number.append(int(index))
        return checkable_user_number

    def compare_numbers(self, checkable_user_number, checkable_number):
        for number in checkable_user_number:
            if number in checkable_number:
                self.cows += 1
        for number in checkable_user_number:
            if number not in checkable_number:
                self.bulls += 1

    def check_win_or_reset(self):
        if self.cows == 4:
            print("You guessed the number in {} turns!".format(self.user_guesses))
            return True
        else:
            self.cows = 0
            self.bulls = 0
            return False

    def main_game(self):
        checkable_number = self.generate_checkable_number()
        while True:
            evaluated_user_input = self.evaluate_user_input("Take a Guess: ")
            if evaluated_user_input == False:
                break

            checkable_user_number = self.convert_user_input(evaluated_user_input)
            self.compare_numbers(checkable_number, checkable_user_number)
            print("You have {} cows and {} bulls".format(self.cows, self.bulls))

            check_game_win = self.check_win_or_reset()
            if check_game_win == True:
                break

            self.user_guesses += 1

def main():
    print("Welcome to bulls and cows, you have to guess the number\nTo quit type 'quit'")

    executable = BullsandCows()
    executable.main_game()
if __name__ == '__main__':
    main()
