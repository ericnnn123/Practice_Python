def FindDivisors(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
    else:
        print("You cannot divide by that number.")
try:
    print("Enter a number to find all of its divisors: ")
    x = int(input())

    print("")
    FindDivisors(x)
except ValueError:
    print("This is not a number.")
