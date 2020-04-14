total_price = 0
count = 0
num_of_iterations = int(input())
while count < num_of_iterations:
    price = float(input())
    total_price += price 
    count += 1

print("Total Price: ", total_price)
print("Average Price: ", total_price / count)