#7.Script to concatenate the following  dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
#ANOTHER PROCESS:
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4 = {}
for i in d1:
    d4[i]=d1[i]
for j in d2:
    d4[j]=d2[j]
for k in d3:        
    d4[k]=d3[k]
print(d4)
#o/p-{1:10,2:20,3:30,4:40,5:50,6:60}         


