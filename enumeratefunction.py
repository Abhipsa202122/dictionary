#The enumerate() function returns an enumerate object that attaches a counter variable to the dictionary’s keys and makes looping over the dictionary easily.
dict1 = {'a':1,'b':2,'c':3}
def count_keys(dict):
    count = 0
    for i in enumerate(dict):
        count += 1
    return count
print(count_keys(dict1))
#nested get():
test_dict = {'Gfg':{'is':'best'}}   
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')  
# printing result
print("The nested safely accessed value is :  " + str(res))
#
a={"abhi":{"is":"boy"}}
print(str(a))
b=a.get("abhi",{}).get("is")
print(str(b))