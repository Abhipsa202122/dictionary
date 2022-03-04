#
d1={1:10,2:20}
d2={3:30,4:40}
d1.update(d2)
print(d1)
#
a={1:2,2:20,3:30,4:56}
d={}
for i in a:
    if a[i]%2!=0:
       d.update(a)
       d[i]=a[i]
    print(d)   
         
    