import os.path

class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.readline_count = {}

        self.read_file()

    def read_file(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line in self.readline_count:
                    self.readline_count[line] += 1
                else:
                    self.readline_count[line] = 1

        self.print_dictionary()

    def print_dictionary(self):
        print(self.readline_count)

def main():
    while True:
        file = str(input("Enter a file path to read from: "))
        file_path = os.path.normpath(file)
        if os.path.exists(file_path):
            print("File Exists")
            ReadFile(file_path)
            break
        else:
            print("...This file doesn't exist, enter one that does...")

if __name__ == "__main__":
    main()
