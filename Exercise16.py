from random import *
import string

def evaluate_input(question):
    available_choices = ["y", "n"]
    while True:
        string_input = str(input(question).lower())
        if not string_input.isalpha():
            print("This is not a choice.")
        elif (string_input not in available_choices):
            print("This is not a choice.")
        else:
            return string_input
            break

def evaluate_number_input(question):
    try:
        while True:
            integer_input = int(input(question))
            if integer_input < 1:
                print("You have to have at least 1.")
            else:
                return integer_input
                break
    except ValueError:
        print("This is not a number")

class GeneratePassword():
    def __init__(self, choice_letters, choice_numbers, choice_symbols, choice_length):
        self.choice_letters = choice_letters
        self.choice_numbers = choice_numbers
        self.choice_symbols = choice_symbols
        self.length = choice_length

    def evaluate_answers(self):
        character_choice = ''
        if self.choice_letters == "y":
            character_choice += string.ascii_letters

        if self.choice_numbers == "y":
            character_choice += string.digits

        if self.choice_symbols == "y":
            character_choice += string.punctuation
        self._generate_password(character_choice)

    def _generate_password(self, character_choice):
        password = "".join(choice(character_choice) for x in range(self.length))
        print(password)


def main():
    choice_letters = evaluate_input("Would you like letters? y or n: ")
    choice_numbers = evaluate_input("Would you like numbers? y or n: ")
    choice_symbols = evaluate_input("Would you like symbols? y or n: ")
    choice_length = evaluate_number_input("How long would you like the password to be? ")

    choices = GeneratePassword(choice_letters, choice_numbers, choice_symbols, choice_length)
    choices.evaluate_answers()

if __name__ == "__main__":
    main()
