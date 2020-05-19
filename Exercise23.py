class FileOverlap:
    def __init__(self, first_file, second_file):
        self.first_file = first_file
        self.second_file = second_file

        self.first_list = []
        self.second_list = []
        self.overlapped_list = []

    def execute(self):
        self.copy_first_file()
        self.copy_second_file()
        self.write_new_file()

    def copy_first_file(self):
        with open(self.first_file, 'r') as file:
            for line in file:
                self.first_list.append(int(line))

    def copy_second_file(self):
        with open(self.second_file, 'r') as file:
            for line in file:
                self.second_list.append(int(line))

    def write_new_file(self):
        with open("write_new_file.txt", 'w') as new_file:
            for element in self.first_list:
                if element not in self.second_list:
                    self.overlapped_list.append(element)

            for item in self.overlapped_list:
                new_file.write(str(item) + '\n')

def main():
    first_file = "first_file.txt"
    second_file = "second_file.txt"

    file_overlap = FileOverlap(first_file, second_file)
    file_overlap.execute()

if __name__ == "__main__":
    main()
