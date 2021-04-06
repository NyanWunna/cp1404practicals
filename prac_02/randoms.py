import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2, 5))  # line 3

# FOR LINE 1
# I saw a random integer being generated between 5 and 20 inclusive.
# The smallest number I could have seen was 5 and the largest was 20.

# FOR LINE 2
# I saw a random odd integer being generated between 3 and 9 inclusive.
# The smallest number I could have seen was 3 and the largest was 9.

# FOR LINE 3
# I saw a random value with 15 decimal places being generated between 2.5 and 5.5.
# The smallest number I could have seen was 2.500000000000000 and the largest was 5.500000000000000

def main():
    print(random.randint(1,100))
main()