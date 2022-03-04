#21.
d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l=[]
for i in d1:
    for a,b in i.items():
        if b not in l:
           l.append(b)
print (l)