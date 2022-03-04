#a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
#a={"s001":20,"s00 2":40}
'''b={}
for i in (a):
    for j in a[i]:
        b.append(a[i][j])
    print(b)'''    
a= {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

for key,values in list(a.items()):
    print(key,values,list)
    word = ""
for i in key:
    #print(i,key[i])
    if i != " ":
       word += i
print(word)
a[word] =a.pop(key)

print(a)