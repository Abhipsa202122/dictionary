"""sentence = ['this','is','a','sentence']
sent_str = ""
for i in sentence:
    sent_str += str(i) + "-"
sent_str = sent_str[:-1]
print(sent_str)
#my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my_lst_str = ''.join(map(str, my_lst))
#print(my_lst_str)
#'12345678910'
a=[1,2,3,4,5,7]
s=""
for i in a:
    s=s+str(i)
#s=s[:-1]
print(s)
a=[1,2,3,4,5,7]
str=""
i=0
while i<len(a):
    print(a[i]+str[i])
    i+=1 
#adjacent"""
a=[1,2,3,4,5,7]
i=0
while i<len(a):
    print(str(a[i])+str(a[i+1]))
    #print(b)
    i+=2       