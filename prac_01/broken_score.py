"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if 90 > score > 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")