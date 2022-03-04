a=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
b=[]
for i in (a):
    if a[i] not in b:
       b.append(a[i])
    #i+=1
print(b)
        