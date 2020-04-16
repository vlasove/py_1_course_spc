d = dict()
d = {}

d[123] = "New element"
d[124] = "New element2"
print(d)

del d[124]
print(d)

elem = d.pop(123)
print(d, elem)
#print(d[125])