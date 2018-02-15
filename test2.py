
l = [('3', '20'), ('1', '50'), ('2', '50')]

total = sum(int(x[1]) for x in l)
#total = sum(filter(lambda i: isinstance(i, int), l))
print(total)

