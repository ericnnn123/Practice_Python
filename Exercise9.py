from random import randint

number = randint(1,9)

print("There is a number in between 1 and 9, you have to guess it.")

def GuessNumber(n):
    cont = True
    level = 1
    while cont:

        #answer validation
        checkinput = True
        while checkinput:
            guess = input("Guess the number: ")
            if guess.lower() == "exit":
                checkinput = False
                break
            elif guess.isdigit():
                checkpoint = False
                guess = int(guess)
                break
            else:
                print("This isn't a number...")
        #check answer and give feedback
        if guess == "exit":
            print("You left after {} turns".format(level))
            break
        elif guess < n:
            print("Higher")
        elif guess > n:
            print("Lower")
        elif guess == n:
            print("You guessed the number in {} turns!".format(level))
            cont = False
        level += 1

GuessNumber(number)
