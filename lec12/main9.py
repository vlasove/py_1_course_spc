def linear(b,c):
    if b == 0:
        return "корней нет"
    else:
        return "один корень"

def quadratic(a,b,c):
    d = b**2 - 4*a*c 
    if d >0 :
        return "два корня"
    elif d == 0:
        return "один корень"
    else:
        return "корней нет"
        
def solve(a,b,c):
    if a == 0:
        return linear(b,c) 
    else:
        return quadratic(a,b,c)


A =int(input())
B =int(input())
C =int(input())

print(solve(A,B,C))