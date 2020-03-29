"""tuple data type is almost indentical to the list data type,
except in two ways. First, tuples are types with parentheses.
Secondly, tuples are immutable, meaning thier values cannot be modified.
"""
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
len(eggs)

"""
#This will cause a TypeError
eggs = ('hello', 42, 0.5)
eggs[1] = 99
"""

#tuple
type(('hello',))
#str
type(('hello'))

"""
tuples are used to show anybody reading that code, that you don't 
intend for the values to change.
"""
