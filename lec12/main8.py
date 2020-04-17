def horse_move(X1:int, Y1:int , X2:int , Y2:int) -> bool:
    return (abs(X1 -X2) == 2 and abs(Y1-Y2) == 1) or (abs(Y1-Y2) == 2 and abs(X1-X2) == 1)




X1s = int(input())
Y1s = int(input())
X2s = int(input())
Y2s = int(input())

if horse_move(X1s, Y1s, X2s, Y2s) == True:
    print("ДА")
else:
    print("НЕТ")

