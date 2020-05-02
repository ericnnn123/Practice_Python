from random import sample

a = sample(range(1, 50), 30)
print(a)

def RemoveDuplicates(l):
    numbers = set()
    for i in l:
        numbers.add(i)
    numbers = list(numbers)
    print(numbers)

RemoveDuplicates(a)
