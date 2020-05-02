class ReverseString():
    def __init__(self, user_input):
        self.user_input = user_input

    def execute(self):
        self.convert_string_to_list(self.user_input)

    def convert_string_to_list(self, user_input):
        user_input_list = self.user_input.split()
        self.reverse_list(user_input_list)

    def reverse_list(self, user_input_list):
        reversed_list = user_input_list[::-1]
        self.convert_list_to_string(reversed_list)

    def convert_list_to_string(self, reversed_list):
        new_converted_string = ' '.join(reversed_list)
        print("\nThis is your string in reverse: ")
        print(new_converted_string)


def main():
    print("Enter in a string to reverse it: ")
    reversable_string = str(input()).lower()

    reverse_string = ReverseString(reversable_string)
    reverse_string.execute()

if __name__ == '__main__':
    main()
