def CheckPrimality(num):
    newlist = []
    for x in range(1,num+1):
        if num % x == 0:
            newlist.append(int(x))
    print("Divisors of {}: {}".format(num,newlist))

    if len(newlist) == 2:
        print("This number is prime")
        return True
    else:
        print("This number is not prime")
        return False


while True:
    try:
        checkNum = int(input("Enter a number to check its primality: "))

        CheckPrimality(checkNum)
        break
    except ValueError:
        print("This is not a number")
