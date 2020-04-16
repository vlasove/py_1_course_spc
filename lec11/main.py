# file_handler = open("input.txt", 'r')
# print("First read",file_handler.read())
# print("Second read", file_handler.read())
# file_handler.close()

with open("input3.txt", 'r') as file_handler:
    #print(file_handler.read())\
    print(file_handler.readlines())
    for line in file_handler.readlines():
        print(line)
        #line.split() --> ["2", "3", "4", "5", "6"]

print('After with block')

print(dir('he'))