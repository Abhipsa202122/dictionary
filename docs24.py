#24.Write a Python program to combine values in python list of dictionaries.
d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d1={}
for i in d:
    if i['item'] in d1.keys():
       d1[i['item']]+=i['amount']
    else:
       d1[i['item']]=i['amount']
print(d1)