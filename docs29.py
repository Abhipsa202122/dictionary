#Q29.Write a Python program to sort a list alphabetically in a dictionary
num = {'a': [2, 3, 1], 'b': [5, 1, 2], 'c': [3, 2, 4]}
sorted_dict = {x:sorted(y)for x, y in num.items()}
print(sorted_dict)