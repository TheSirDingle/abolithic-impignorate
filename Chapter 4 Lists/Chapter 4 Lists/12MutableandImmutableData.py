#strings are an immutable, meaning it can't be changed 
#list values are mutable, meaning it can be changed. Such as adding, removing, etc

"""
Causes a TypeError 
name = 'Zophie a cat'
name[7] = 'the'
"""

#proper way: 
name = 'Zophie a cat'
#0:7 and 8:12 are the characters we don't want to repalce
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

#to modify the original list values you'll have to do something like this
#this throws out the original values, and repalces it 1 by 1 with the new values
#first it takes away the og values, and after that the new values are appeneded 
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)
