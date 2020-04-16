with open('input3.txt', 'a') as file_handler:
    file_handler.write("\nHello from python script!2")
    file_handler.writelines(["\nFirst Row", "\nSecond Row"])