#a="my name is abhipsa"
#d={}
#c=0
#s=a.split()
'''for i in a:
    for j in a[i]:
        if i in d:
           d[i]+=1
        else:
           d[i]=1
           c+=1
           d.append(c)      
print(d) '''
#i=0
#while i<len(s):
#    print(d,""+s[i],i+1,end="")
    #p=s[i]+str(i+1)
    #d.append(p)
#    i+=1
#print(d)
test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
a="my name is abhipsa"
d=[]
c=0

#
'''a=[1,2,3,4,5,6,7,8,9,10]
d={}
for i in a:
    if i[0] not in d.keys():
       d.update({i[0]:[i[1]]})
    elif i[0] in d.keys():
        d[i[0]].append(i[1])
print(d)'''           
            