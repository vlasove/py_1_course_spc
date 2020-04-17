def zeros(a):
    print(1/a)
    #print("1" + a)

try:
    zeros(1)
    name = "asdasd"
    name[1112]

except ZeroDivisionError as z_err:
    print("HAPPEND ZERO DIVISION. DON'T USER ZEROES", z_err)
except TypeError as t_err:
    print("HAPPEND ERROR WITH TYPES. USE INT", t_err)
else:
    print("ELSE BLOCK!")
finally:
    print("USER ID 10 SUCCESS WORKS WITH TRY\EXCEPT BLOCK # 25012")

print('AFTER TRY EXCEPT')