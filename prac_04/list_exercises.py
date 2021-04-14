numbers = []
for i in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)
max_number = max(numbers)
min_number = min(numbers)
average_number = sum(numbers)/len(numbers)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min_number))
print("The largest number is {}".format(max_number))
print("The average of the numbers is {}".format(average_number))