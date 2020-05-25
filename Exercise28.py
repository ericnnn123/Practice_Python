
class MaxOfThree:
    def __init__(self):
        self.list_of_three = []

    def execute(self):
        self.get_list_of_three()
        self.get_max(self.list_of_three[0], self.list_of_three[1], self.list_of_three[2])
        self.print_max()

    def get_list_of_three(self):
        limit = 0
        while limit < 3:
            while True:
                try:
                    number_input = int(input("Enter in three different numbers: "))
                    if number_input not in self.list_of_three:
                        self.list_of_three.append(number_input)
                        break
                    else:
                        print("You already entered that number.")
                except ValueError:
                    print("You can only enter in numbers.")
            limit += 1

    def get_max(self, a, b, c):
        if a > b and a > c:
            self.result = a
        elif b > a and b > c:
            self.result = b
        elif c > a and c > b:
            self.result = c
        else:
            self.result = "An error occurred"


    def print_max(self):
        print("Max value is: {}".format(self.result))

def main():
    program = MaxOfThree()
    program.execute()

if __name__ == "__main__":
    main()
