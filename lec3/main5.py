# Условный оператор
# if expression:
#     body
# else:
#     else_body

# if - операторное слово 
# expression - условное выражение
# body - тело условного оператора 
# else - операторное слово (соотносится с ближайшим if)
# else_body -  тело оператора else 


age = int(input())

if age > 18:
    print("WELCOME TO OUR SERVICE!")
    print("U can use payments!")
    if "Bob" == "Bob":
        print("BOB IS BOB!")
else:
    print("WELCOME TO OUR DEMO VERSION OF SERVICE!")

print("AFTER IF BLOCK")
