number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items !=0:
    for n in range(0,number_of_items):
        item_price = float(input("Price of item: "))
        total_price += item_price
    if total_price > 100:
        discounted_price = total_price*0.1
        final_price = total_price-discounted_price
        print("Total price for {} items is ${:.2f}".format(number_of_items, final_price))
        break
    elif 0< total_price <= 100:
        print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
        break
    else:
        print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))