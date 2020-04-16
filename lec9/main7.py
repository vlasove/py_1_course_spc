p = [1,2,3]

for item in p:
    p.append(item)
    if len(p) > 100:
        break

print(p)

