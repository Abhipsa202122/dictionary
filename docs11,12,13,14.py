#11.script to merge 2 python dictionaries:
d1 = {'a': 10, 'b': 20}
d2 = {'x': 30, 'y': 40}
dic = {}
for i in (d1,d2):
    dic.update(i)
print(dic)
#o/p:{'a': 10, 'b': 20,'x': 30, 'y': 40}
#12.sum of the values in dictionary:
d1={'a': 10, 'b': 20,'x': 30, 'y': 40}
s=0
for i in d1:
    s=s+d1[i]
print(s)    
#13.multiplication of the value:
d1={'a': 10, 'b': 20}
m=1
for i in d1.values():
    m=m*i
print(m)
#o/p-200
#14.remove a key from dictionary:
d1={'a': 10, 'b': 20,'c': 30, 'd': 40}
if "b" in d1:
    del d1["b"]
print(d1)
#o/p-{'a': 10,'c': 30, 'd': 40}    
  
        