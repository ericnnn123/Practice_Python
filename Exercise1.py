#get initial inputs
print("What is your name?")
nameInput = input()
print("What is your age?")
ageInput = int(input())

#define function that adds 100 years to age
def hundredyearslater(name, age):
    futureAge = age + 100
    futureAge = str(futureAge)
    print("Hello {}, you will be {} in 100 years".format(name, futureAge))
#call the function
hundredyearslater(nameInput, ageInput)

#grab random input
print("Enter a random number:")
iterate = int(input())

#function that prints x amount of strings
def multiplyanswer(number):
    for _ in range(number):
        hundredyearslater(nameInput, ageInput)
        print("\n")
multiplyanswer(iterate)
