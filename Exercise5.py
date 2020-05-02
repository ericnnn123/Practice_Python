import random

a = random.sample(range(0, 100), random.randint(0, 25))
b = random.sample(range(0, 100), random.randint(0, 25))

newList = []
def ListComparer(list1, list2):
    for x in list1:
        if x in list2:
            newList.append(x)
    for y in list2:
        if y in list1:
            newList.append(y)

def ListComparerOpposites(list1, list2):
    for x in list1:
        if x not in list2:
            newList.append(x)
    for y in list2:
        if y not in list1:
            newList.append(y)

def RemoveDuplicates(x):
    if not x:
        return "List is empty."
    else:
        return list(dict.fromkeys(x))


ListComparer(a, b)

print("Original Lists: \n {} \n {}".format(a, b))
print("List Similarities: \n {}".format(RemoveDuplicates(newList)))
