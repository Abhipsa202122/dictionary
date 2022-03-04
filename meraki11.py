#11.Merge 2 python:
d1={"a":10,"b":20}
d2={"c":30,"d":40}
d={}
for i in (d2,d1):
    d.update(i)
print(d)
#o/p-{"c":30,"d":40,"a":10,"b":20}    