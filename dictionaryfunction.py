#copy():
d={"day":25,"month":2,"year":2022}
a=d.copy()
print(a)
#o/p-{'day': 25, 'month': 2, 'year': 2022}
#fromkeys():
l=[1,2,3,4]
b=dict.fromkeys(l)
print(b)
#o/p-{1: None, 2: None, 3: None, 4: None}
#Accessing items:
a={'day': 25, 'month': 2, 'year': 2022}
x=d["month"]
y=a.items()
print(x,y)
#o/p-2
a={"a":{1:20,2:30},"b":{4:10,3:20}}
c=a[b][3]
print(c)

