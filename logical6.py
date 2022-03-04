#one list to convert to dictionary
a=[1,2,3,4,5,6,8,9,10]
c=d={}
for i in a:
    #if d["c"+c]=[]:
    for j in range(i,i+3): 
        c.setdefault(i,[]).append(j)
print(c)
'''a=[1,2,3,4,5,6,7,8,9,10]
#c=0
d={}  
for i,j in a: 
    d.setdefault(i,[]).append(j)
    #d["c"+c(i)]=[]    
    #d.append(i)    
print(d)'''