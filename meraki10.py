#10.Total count: 
dict1={'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
c=0
for i in dict1:
    c=c+len(dict1[i])
print(c)    