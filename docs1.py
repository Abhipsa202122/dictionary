#d1={'a': 100, 'b': 200, 'c':300}
#d2={'a': 300, 'b': 200, 'd':400}
#d3={}
#for i,j in d1.items():
 #   for x,y in d2.items():
  #      if i==x:
 #          d3[i]=(j+y)
#print(d3)
#DOCS QUESTIONS START:
#1.2 Dictionary adding value:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
for i in d1 :
    if i in d2 :
        d2[ i ] = d2[ i ] +d1[ i ]
    else :
        d2[ i ] = d1[ i ]
print(d2)
#o/p-{'a': 400, 'b': 400, 'd': 400,'c':300}

