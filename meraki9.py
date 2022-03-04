#9.frequency question:
a="MISSISSIPPI"
b={}
for i in a:
    if i in b:
       b[i]+=1
    else:
       b[i]=1
print(b)
#o/p:{"M":1,"I":4,"S":4,"P":2}           