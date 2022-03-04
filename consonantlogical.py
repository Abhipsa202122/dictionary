a=input("Enter word: ")
vowels=['a','e','i','o','u']
v=0
c=0
#k={}
for i in a:
    if i in vowels:
        #k.append(i)
        v+=1
    elif i!=' ':
        #k.append(i)
        c+=1

print("Vowels: ",v)
print("Consonants: ",c)   
       