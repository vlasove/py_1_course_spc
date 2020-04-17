#REGULAR EXPRESSIONS
import re

addresses = "qwert@mail.ru, abcd@gmail.com , test@myspace.su"
list_words = re.findall('@\w+.(\w+)', addresses)
print(list_words)
