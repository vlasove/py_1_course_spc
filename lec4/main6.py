total_price = 0
price = float(input())
while price > 0:
    total_price += price
    price = float(input())

print('Total Price is:', total_price)