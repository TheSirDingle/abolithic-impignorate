#In and out operators used in expressions and connect two values. 
#They evaluate to a Boolean value.

#checks if howdy is inside the list, and outputs either True or False. 
print('howdy' in ['hello','hi','howdy','heyas'])

#you can type a list and check if certain indexes are in it.
spam = ['hello','hi','howdy','heyas']
#checks if cat is inside the list spam
print('cat' in spam)
#checks if howdy is not inside the list spam
print('howdy' not in spam)
print('cat' not in spam)

#mutiple assignment trick

#lets you assign multi variables with the values in a list in one line of code
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

#instead of 
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

#Augmented Assignment Operators

"""
operators like spam = spam + 1 or spam = spam - 1 are instead 
spam += 1 or spam -= 1
"""

"""
list of augumented operators +=,-=,*=,/=,%=
"""

dam = 54
dam += 1
dam -= 1

tram = 'hello'
tram += ' world!'
print(tram)
