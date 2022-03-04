'''a=[{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"six":"9"},{"seven":"7"}]
b=[]
for i in range(len(a)):
    if a[i] not in a[i+1]:
        b.append(a[i])
 
print(b)'''
Langlist=[{"first":1},{"second":2},{"third":1},{"four":5},{"six":9},{"seven":7}]
#Langlist = [{"C#" : 1}, {"Rust" : 2}, {"C++" : 3}, {"Rust" : 2}, {"python" : 4},{"python" :4}] 
result_dict=[]
#removing the duplicate entry
for i in range(len(Langlist)):
    if Langlist[i] not in Langlist[i + 1:]:
        result_dict.append(Langlist[i])
 
print('after Removing duplicate from list of dictionary =\n',result_dict)