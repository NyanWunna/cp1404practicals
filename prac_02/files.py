def main():
    NAME_FILE = "name.txt"
    name_file = open(NAME_FILE, "w")
    name = input("Enter name: ")
    print(f"{name}", file=name_file)

    name_file.readline(2)
    name_file.close()

    NUMBER_FILE = "numbers.txt"
    number_file = open(NUMBER_FILE, "r")
    first_line_str = input_file.readline()
    second_line_str = input_file.readline(2)
    total=first_line_str+second_line_str
    print(f"{total}", file=input_file)

main()