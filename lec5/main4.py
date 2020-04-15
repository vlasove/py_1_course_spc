n = int(input())
sum_nums = 0


for i in range(n):
    num = int(input())
    if i % 2 == 0:
        sum_nums += num 
    else:
        sum_nums -= num 

print(sum_nums)