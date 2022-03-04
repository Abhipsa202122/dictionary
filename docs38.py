'''Q38.. Write a Python program to drop empty Items from a given Dictionary. 
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}'''

d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d2= {}
for i,j in d1.items():
    if j > 170:
       d2[i] = j
print(d2)