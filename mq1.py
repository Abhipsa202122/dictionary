#Meraki questions 1:
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
b={}
for i in dic1:
    b[i]=dic1[i]
for j in dic2:
    b[j]=dic2[j]
for k in dic3:    
    b[k]=dic3[k]
print(b)
#another process using update method:
#Add one or more items into existing dictionary
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
 