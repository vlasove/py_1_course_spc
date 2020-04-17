def add(a:int):
    def add_new(b:int):
        return a + b 
    return add_new


adder_2 = add(2) # add_new :-> return 10 + b
print(adder_2)
print(adder_2(5))

print(add(2)(3))




mult(2)(3)(4) # 2*3*4 - > 24

