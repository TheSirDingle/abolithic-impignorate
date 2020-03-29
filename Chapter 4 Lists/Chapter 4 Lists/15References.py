"""
this doesn't change cheese to 100 becuase they're different 
variables that store different values
"""
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

#doesn't work the same way in list because you're technically assigning a list reference
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)

#Passing References
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
#this adds the parameter of eggs to the list of spam
eggs(spam)
#this outputs [1,2,3,'Hello']
print(spam)
