import random


def print_lines():
    lines = []
    while len(lines) != 6:
        random_number = random.randint(1, 45)
        if random_number not in lines:
            lines.append(random_number)
            lines.sort()
    for i in lines:
        print("{:>2d}".format(i), end=" ")


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(0, number_of_quick_picks):
        print_lines()
        print("\n")


main()