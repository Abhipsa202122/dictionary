#22.
d = {'1':['a','b'], '2':['c','d']}
a,b = d.values()
for i in a:
    for j in b:
        print(i+j)