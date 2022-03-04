i=1
count=0
a=int(input("enter any number="))
while count<a:
    factor=0
    j=1
    while j<=i:
        if i%j==0:
            factor=factor+1
        j=j+1 
    
    if factor==2:
        x=i
        count=count+1
    i+=1
print(x)