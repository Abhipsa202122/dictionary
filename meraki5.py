#5.2 list convert to dictionary:
a=["one","two","three","four","five","six"]
b=[1,2,3,4,5,6]
c={}
for i in a:
    for j in b:
        c[i]=j
        b.remove(j)
print("dic is",(c))
#o/p:{“one”:1,”two”:2,”three”:3,”four”:4,”five”:5,"six":6}
#another process in zip method:
a=["one","two","three","four","five","six"]
b=[1,2,3,4,5,6]
r=dict(zip(a,b))
print(r) 