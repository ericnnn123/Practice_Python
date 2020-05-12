class WriteToFile:
    def __init__(self, name_input, line_content, lines):
        self.file_name = name_input + '.txt'
        self.line_content = line_content
        self.number_of_lines = lines

        self.write_file()

    def write_file(self):
        with open(self.file_name, 'w') as file:
            for _ in range(self.number_of_lines):
                file.write(str(self.line_content) + "\n")


def main():
    name_input = str(input("What would you like the file name to be? "))
    line_content = str(input("What would you like to write in this file? "))
    while True:
        try:
            lines = int(input("How many lines? "))
            WriteToFile(name_input, line_content, lines)
            break
        except ValueError:
            print("Enter in a real number please")

if __name__ == "__main__":
    main()
