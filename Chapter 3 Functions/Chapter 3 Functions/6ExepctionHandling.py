#Aaron Stockman

#without the try function it will output a divided by zero error 
#with it, it will output all the calls, and output zero as an error 
def spam(divideBy):
    #try statement allows you too handle certain error, so that they don't crash the program
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument.')

print(spam(2))
print(spam(12))
#Invalid Argument
print(spam(0))
print(spam(1))

#This format causes the function to stop at spam(0) 
try:
 print(spam(2))
 print(spam(12))
 print(spam(0))
 print(spam(1))
 
except ZeroDivisionError:
 print('Error: Invalid argument.')