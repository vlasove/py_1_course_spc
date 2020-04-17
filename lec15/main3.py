def add(a,b):
    return a + b 

def caller(my_func):
    print('Result of:', my_func(2,3))


caller(add)

func_list = [caller, add]

func_list[1](2,3)