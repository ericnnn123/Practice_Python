def OddorEven(x):
    if x % 4 == 0:
        print("This number is divisible by 4!")
    elif x % 1 == 0:
        print("This number is odd")
    elif x % 2 == 0:
        print("This number is even")

def CheckDivisibility(x, y):
    if x % y == 0:
        print("This number is divisible by {}".format(y))
    else:
        print("This number is not divisible by {}".format(y))

while True:
    try:
        num = int(input("Enter in a number: "))
        checkNum = int(input("Check divisibility: "))

        print("\n")
        OddorEven(num)
        CheckDivisibility(num, checkNum)
    except ValueError:
        print("Not a number")
