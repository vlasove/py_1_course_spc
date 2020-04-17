def super_func(a,b, c=1, d=2):
    return a**2 + b**2 + (c+d)**3

print(super_func(1,2,3,4))
print(super_func(10,20, d = 30))
print(super_func(100,200))
print(super_func(10,20))