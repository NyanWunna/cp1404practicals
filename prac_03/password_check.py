MINIMUM_LENGTH = 6

def get_password():
    password = input("Enter password: ")
    return password

def is_valid_password(password):
    while True:
        if len(password) >= MINIMUM_LENGTH:
            covered_password = "*" * len(password)
            print(f"{covered_password}")
            break
        else:
            print("Invalid Password")
            password = input("Enter password: ")

def main():
    password = get_password()
    is_valid_password(password)

main()
