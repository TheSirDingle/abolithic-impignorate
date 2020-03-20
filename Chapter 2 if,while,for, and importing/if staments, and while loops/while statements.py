#Aaron Stockman
#While statments,  breaks, and continues 

#while loops are statements that repeat itself until the statement is false 

#repeats spam print 20 times 
spam = 0
while spam < 20:
    print('SCREW YOU REEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    spam = spam + 1

name = ''
while name != 'your name':
 print('Please type your name.')
 name = input()
print('Thank you!')

while True:
    print('Please type your name again.')
    name = input()
    if name == 'your name':
        #if the statement is true it breaks out of the while statement to print statement
        break
print('Thank you again!')


while True:
 print('Who are you?')
 name = input()
 if name != 'Joe':
     #Loop doesn't continue if name isn't joe. break statement jumps back to start of while loop and reevaluates the loop
     continue
 print('Hello, Joe. What is the password? (It is a fish.)')
 password = input()
 if password == 'swordfish':
     break
 else:
     print('Wrong Password, please enter again')
     continue
print('Access granted.') 
