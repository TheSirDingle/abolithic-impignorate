#Aaron Stockman

#remove function allows you to remove certain values inside a list
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
#attempting to delete a value that's not inside the list will result in a ValueError

#if you have mutiple of the same value, it will only delete the first value
tram = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
tram.remove('cat')
print(tram)
#del statement is good when you know the index of the value
#while the remove statement is good when you know the value

#sorts #'s from least to greatest 
ram = [2, 5, 3.14, 1, -7]
ram.sort()
print(ram)

#sorts words in alphabetical order (does uppercase before lowercase)
mam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
mam.sort()
print(mam)

#reverse sorts the list
dam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
dam.sort(reverse=True)
print(dam)

#NOTES
#You cannot capture the return value EX: spam = spam.sort()
#You cannot sort list that have both numerical values and string values
#It uses ASCIIbetical order inside of regular order, which means uppercase comes before lowercase
"""
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
"""