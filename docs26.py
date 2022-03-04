'''my_dict = {'A':[1,2,3],'B':[4,5,6],'C':[10,20,30], 'D': [11, 22, 33]}
all_keys = list(my_dict.keys()) # ('A', 'B', 'C')
lst = list(my_dict.values())
for key in all_keys:
    print(key+" ", end='')

print("\n")

L = 0
while L < len(lst):
    for i in range(0, len(lst)):
        for j in range(L, len(lst[i])):
            print(lst[i][j], end = ' ')
    break

print("\n")

L += 1'''
#26.
a= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print(*list(a.keys()))
a=(list(a.values()))
for i in range(len(a)):
    print(*(a[i]))
