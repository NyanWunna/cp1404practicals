"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("try again")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    # A ValueError will occur when the input is not an integer
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    # A ZeroDivisionError will occur when the denominator is zero (denominator==0)
    print("Cannot divide by zero!")
print("Finished.")