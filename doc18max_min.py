#18.maximum & minimum:
n={"a":20,"b":30,"c":10,"d":40}
max=0
min=n[0]
for i in n:
    if n[i]<min:
       min=n[i]
       #min.append()
    elif n[i]>max:
       max=n[i]
       #max.append() 
print(min)
print(max)            