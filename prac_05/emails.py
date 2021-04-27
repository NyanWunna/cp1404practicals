def main():
    email = input("Email: ")
    data = {}

    while email != "":
        name_part = email.split("@")[0]
        email_part = name_part.split(".")
        name = "".join(email_part).title()
        name_confirm = input(f"Is your name {name}? y/n").lower()
        if name_confirm == "n" or name_confirm == "":
            name = input("Name: ")
        data[email] = name
        email = input("Email: ")
    for x, y in data.items():
        print(f"{y} ({x})")


main()
