import random

list1 = random.sample(range(0,100), 10)
list2 = random.sample(range(0,100), 10)

newList = [x for x in list1 if x in list2]

print(list1)
print(list2)
print(newList)
