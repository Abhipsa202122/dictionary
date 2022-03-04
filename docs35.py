a={'key1': 1, 'key2': 2, 'key3': 2}
b={'key1': 1, 'key2': 2}

for i,j in a.items():
    if i in b and a[i]==b[i] :
       print(i,':',j ,'is present in both ')