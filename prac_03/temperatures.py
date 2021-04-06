"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def convert_C_to_F():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_F_to_C():
    fahrenheit = float(input("Celsius: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def main():
    MENU = """\tC - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "F":
            fahrenheit = convert_C_to_F()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "C":
            celsius = convert_F_to_C()
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print ("Thank You")


main()