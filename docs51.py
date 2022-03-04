'''Q51.Write a Python program to filter even numbers from a given dictionary values. 
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}'''

d ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for k in d.keys():
    print(k)
    print(d[k])
   # d [k] = [i for i in d[k] if i%2 ==0]
    for i in  d[k]:
        if i%2==0:
           print(i)