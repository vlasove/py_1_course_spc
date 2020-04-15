a_set = set([1,2,3,4,5])
b_set = set([3,4,5,6,7])

c_set = a_set.intersection(b_set) # b_set.intersection(a_set)
print("Intersection:", c_set)

d_set = a_set.union(b_set) #b_set.union(a_set)
print("Union:", d_set)

e_set = a_set - b_set #b_set - a_set
print("Difference A-B:", e_set)

f_set = a_set.union(b_set) - a_set.intersection(b_set)
g_set = a_set ^ b_set  #b_set ^ a_set
print("Symmetric difference:", g_set)


