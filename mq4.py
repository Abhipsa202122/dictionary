dict={1:'NAVGURUKUL',2:'IN',3:{'A':'WELCOME','B':'To','C':'DHARAMSALA'}}
#for i in dict:
#    dict.pop('A')
#print(dict)
#or i in dict:
#    dict[i].pop(3,None)
#print(dict)
del dict['A']
print(dict)
data = {
        'key1': 
            {
            'a': 'key1', 
            'b': 'val1', 
            'c': 'val2'
            }, 
        'key2': 
            {
            'a': 'key2', 
            'b': 'val3', 
            'c': 'val4'
            }, 
        'key3': 
            {  
            'a': 'key3', 
            'b': 'val5', 
            'c': 'val6'
            }
        }

for key in data:
    data[key].pop('c',None)

print(data)

