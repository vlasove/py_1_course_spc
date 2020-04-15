while True:
    password1 = input()
    password2 = input()

    if len(password1) < 8 :
        print("Слишком короткий пароль!")
        continue 
    elif "qwe" in password1 or "123" in password1:
        print("Слишком простой пароль!")
        continue 
    elif password1 != password2:
        print("Введенные пароли различаются!")
        continue
    else:
        print("Ну наконец-то!")
        break