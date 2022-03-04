def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

#print( word_count('the quick brown fox jumps over the lazy dog.'))
print(word_count("my name is abhipsa"))
def vowel_count(str):
    count =dict()
    c=dict()
    # Creating a set of vowels
    vowel = set("aeiouAEIOU")
    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:
        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1
        else:
            c=c + 1
            #d.append(count)
            #d.append(c)   
    print("No. of vowels :", count)
    print("no.of consonant",c)
      
# Driver code 
str = "my name is abhi"
  
# Function Call
vowel_count(str)
