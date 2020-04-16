a_list = [1,2,3] * 99
b_list = [1]

b_list.append("hello")
print(b_list)

print("Min:", min(a_list))
print("Sum:", sum(a_list))

a_list[0] = 200
print(a_list)

print(a_list[0])
print(a_list[-1])
print(a_list[64])

a_list.sort(reverse=True)

print(a_list)
print("This count 1:",a_list.count(1))
print(a_list.index(200))


a_list.reverse()
a_list[::-1]

print(dir(a_list))



a_list.append(10)
a_list.insert(10, 200)
