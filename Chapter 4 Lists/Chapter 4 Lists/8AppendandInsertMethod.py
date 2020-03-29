#to add values to a list use the append() and insert() methods 

spam = ['cat', 'dog', 'bat']
#this adds moose the list, but always puts it at the end of the list
spam.append('moose')
print(spam)

tram = ['cat', 'dog', 'bat']
#inserts chicken at index 1, and moves dog over to index 2
tram.insert(1, 'chicken')
print(tram)

"""
the return value of both inset and append are none. 
which means that the list is modified in place
"""

#this will cause an attribute error 
"""
eggs = 'hello'
eggs.append('world')
"""

"""
bacon = 42
bacon.insert(1, 'world')
"""
