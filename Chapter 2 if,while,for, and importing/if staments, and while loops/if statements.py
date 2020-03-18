#Created by Aaron Stockman
#This is a test of if statements, while loops, and a few other function

#type flow statements 
#if statement is true execute, if not then do not execute
#Contains the if keyword, a condition, a colon, and a indented block of code starting on the next line 

#else statement is the block of code that's executed if the if statement is false 
#else contains else keyword, colon, and indented block of code starting on next line

#elif statment is a statement that always follow an if/elif statement 
#provides a condition that is checked only if any other previous conditions were False
#consist of elif keyword, condition, colon, indented block of code starting on next line
name = input('Please enter your name: ')
if name == 'Mary' or 'mary':
    print('Hello Mary')
    password = input('Please enter your password: ')
    if password == 'swordfish' or ' swordfish':
        print('Access Granted')
    else: 
        print('Wrong password.')

name1 = input('Please input name: ')
age = input('please enter your age')
if name1 == 'Alice' or 'alice':
    print('Hi, Alice.')
elif age > 12:
    print('you are not alice, Extermination sequence initiated')
elif age == 12:
    print('you might be her')
elif age > 2000:
    print('that is some nice age serum you have there')

        




