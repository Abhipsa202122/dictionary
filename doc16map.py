#16.map 2 lists into a dictionary:
d1={"a":10,'b':20}
d2={'c':30,'d':40}
d={}
for i in (d2,d1):
    d.update(i)
print(d)
#o/p-{"a":10,'b':20,'c':30,'d':40}    