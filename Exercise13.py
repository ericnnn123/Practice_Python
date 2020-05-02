def fibonacci(n):
    fibo = [0, 1]
    for x in range(0, n-2):
        equation = fibo[-1] + fibo[-2]
        fibo.append(equation)
    print(fibo)


try:
    number = int(input("How many fibonacci numbers would you like to generate?: "))

    fibonacci(number)
except ValueError:
    print("This is not a number")
