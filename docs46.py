'''Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
Original list:
[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
String values of a given dictionary, into float types:
[{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]'''


l=[{'x':'10','y':'20','z':'30'},{'p':'40','q':'50','r':'60'}]
a,b=l
ans1={}
ans2={}
final_list=[]
for i,j in a.items():
    d={i:int(j)}
    ans1.update(d)
for i,j in b.items():
    d1={i:float(j)}
    ans2.update(d1)
    final_ans=ans1,ans2
for i in final_ans:
    final_list.append(i)
print(final_list)