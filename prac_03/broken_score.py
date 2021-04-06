"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid"
    else:
        if 90 > score > 50:
            result = "Passable"
        elif score >= 90:
            result = "Excellent"
        else:
            result = "Bad"
    return result


def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)


def get_random_score():
    score = random.randint(1,100)
    print (f"\nRandom Score: {score}")
    result = check_score(score)
    print(result)


main()
get_random_score()