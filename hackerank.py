n=[2,3,6,6,5]
l=0
i=0
m=0
m2=0
while i<len(n):
    #if n[i] in n[:i]:
     #  n.pop(i) 
    l.append(i)
    print(l)
    while j<len(l):
    #if n[i] in n[:i]:
    #   n.pop(i)
     
       if l[i]>m:
          m2=m
          m=l[i]
       elif l[i]>m2:
            m2=l[i]
        
    i+=1
#print(m)
print(m2)                