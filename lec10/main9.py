d = {"one":1, "two":2, "three":3}

list_keys = list(d.keys())
print(list_keys)

list_values = list(d.values())
print(list_values)

if 3 in d.values():
    print("YESS")

for key in d.keys():
    print(key)

for val in d.values():
    print(val)

for key in d.keys():
    print(key, d[key])

for key, val in d.items(): 
    print( key, val)


a, b, c = (1,2,3)
print(a,b,c)
