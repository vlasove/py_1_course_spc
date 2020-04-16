db_famous = [0] * 2020
db_famous[1965] = "Guido Van Rossum"
db_famous[1970] = "Bjorn Straustroup"
db_famous[1991] = "Python"
db_famous[1997] = "Java"

# dict() - словарь. Коллекция, хранящая МНОЖЕСТВО пар ключ:значение.
db_famous_dict = { 1965: "Guido Van Rossum", 1970:"Bjorn Straustroup", 1991:"Python", 1997:"Java"}
print(db_famous_dict[1965])
print(db_famous_dict[1991])

print(db_famous_dict, len(db_famous_dict))