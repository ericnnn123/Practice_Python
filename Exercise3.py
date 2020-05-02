a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def IterateLessThanFive(list, x):
    newList = []
    for i in list:
        if i < x:
            newList.append(i)
    print(newList)

try:
    num = int(input("Enter a number: "))
    IterateLessThanFive(a, num)
except ValueError:
    print("Enter a number.")
