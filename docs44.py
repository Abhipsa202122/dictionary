#Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
'''Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]'''


d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

res=[]
a,b=d.values()

for i in range(len(a)):
    for j,k in d.items():
        b=({j:k[i]})
        res.append(b)
print(res)