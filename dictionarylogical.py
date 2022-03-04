d = {25:50,30:60}
keys_values=d.items()
d1={str(key): str(value) for key, value in keys_values}
print(d1)
#key to value logical question:
#a={"a":10,"b":20,"c":30}
#b=a.items()
#c={value : key for key, value in a.items()}
#print(c)
#for key, value in b:
 #   print(key,value,b)
a={"a":10,"b":20,"c":30}
#b=a.items()
c={a[i]: i for i in a}
#c={value : key for key, value in a.items()}
print(c)    
'''dict = {(3,4,8):4,(5,6,9):3}
for i in dict:    
    print('output:',(i),dict[i],dict[(5,6,9)])'''
'''a={"a":10,"b":20,"c":30}
d={}
for i in a.items():
    d[i[1]]=i[0] 
    print(d)'''
a="abhipsa"
d={}
c=0
'''for i in a:
    if a=="a" or a=="e" or a=="i" or a=="o"or a=="u":
       c+=1
    else:
        c+=1
        print(c)'''
#x = input("Enter a word: ")  
'''vowels=['a','e','i','o','u']

for vowel in vowels:
    if vowel in x:
       print("Vowels")
    else:
       print("consonant")
def symbol_freq(string):
    symbol_freq_dict = dict.fromkeys(string, 0)
    for i in string:
        symbol_freq_dict[i] += 1
    return symbol_freq_dict
       
def group(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    consonants = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž', 't', 'v']
    string.lower()
    symbol_freq_dict = symbol_freq(string)
    grouped_dict = dict()
    for key, value in symbol_freq_dict:
        if key in vowels:
            grouped_dict['Vowels'].append((key, value))
        if key in consonants:
            grouped_dict['Consonants'].append((key, value))
        else:
            grouped_dict['Other'].append((key, value))
            
            
    return grouped_dict'''
 #define all vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']

#input a string and transform it to lower case
str = input("Enter a string: ")

#define counter variable for both vowels and consonants
v_ctr = 0
c_ctr = 0

#iterate through the characters of the input string 
for x in str:
    #if character is in the vowel list,
    #update the vowel counter otherwise update consonant counter
    if x in vowels:
        v_ctr += 1
    elif x != ' ':
        c_ctr += 1

#output the values of the counters
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)   
       
        
           