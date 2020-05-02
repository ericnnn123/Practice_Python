import random

a = random.sample(range(1,50), 10)

def ListEnds(initialList):
    b = []
    print(initialList)
    b.append(initialList[0])
    b.append(initialList[-1])

    print(b)

ListEnds(a)
