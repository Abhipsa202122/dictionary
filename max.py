n= {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
m1=0
m1s=""
m2=0
m2s=""
m3=0
m3s=""
# n=str(n)
for i in n:
#for i in n:
    if n[i]>m1:
         m3=m2
         m3s=m2s
         m2=m1
         m2s=m1s
         m1=n[i]
         m1s=i
        # m1.append(i)   
    elif n[i]>m2:
         m3=m2
         m3s=m2s
         m2=n[i]
         m2s=i
         #m2.append(i)
    elif n[i]>m3:
         m3=n[i]
         m3s=i
         #m3.append(i)    
    #i+=1
print(m1s)
print(m2s)
print(m3s)

