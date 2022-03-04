#2.frequency question:
a="W3RESOURCES"
b={}
for i in a:
    if i in b:
       b[i]+=1
    else:
       b[i]=1
print(b)
#o/p:{"W":1,"3":1,"R":2,"E":2,"S":1,"O":1,"U":1,"C":1}           