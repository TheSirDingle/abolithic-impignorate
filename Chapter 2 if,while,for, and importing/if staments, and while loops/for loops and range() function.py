#Aaron Stockman
# for loops, range() function 

# for loops allow you to execute a loop only a certain amount of times 

#prints Jimmy Five Times(i) 5 times ranging from i=0 to 4
print ('my name is')
for i in range(5):
    print('Jimmy Five Times(' + str(i) + ')')

#this exectues total = total + num 100 times 
#Causing every integer 0 to 100 to be added to the total 
#ex: 1+99, 2+98 etc. 
print('\nhere is a range function that adds up every number between 0-100')
total = 0 
for num in range(101):
    total = total + num
print(total) 


#range(start,end,interval)
#this prints #'s 12-16s
print('\n here is a range function')
for i in range(12,16):
    print(i)

#range that prints on from 0-10 with intervals of 2
print('\n here is another')
for i in range(0,10,2):
    print(i)

print('\n another one')
for i in range(100, -1, -5):
    print(i)