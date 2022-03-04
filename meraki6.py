#dic = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
#6.remove duplicate keys:
dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
d=[]
r=dict()
'''for i,j in dic.items():
    if i not in r:
        r.append(i)
        
print(r)'''
for i in range(len(dic)):
    if dic[i] not in dic[i+1]:
        d.append(dic[i])
 
print(d)
