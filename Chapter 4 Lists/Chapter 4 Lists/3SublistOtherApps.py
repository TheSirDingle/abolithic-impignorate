#spam[2] is a list with an index (one integer)
#spam[1:4] is a list with a slice (two integer) 
#The first integer is where the slice starts. The second integer is where the slice ends 

spam = ['cat', 'bat', 'rat', 'elephant']
#prints values 0-3
print(spam[0:4])
#prints values 1-2
print(spam[1:3])
#prints values 0 to 2
print(spam[0:-1])
#excludes any value 2 and greater 
print(spam[:2])
#excludes any value 1 and below
print(spam[1:])
print(spam[2:])
print(spam[:])

#Getting list length with len()
tram = ['cat', 'dog', 'moose']
#outputs number of values that are passed through the list variable
print(len(tram))

#Changing values in a list with indexes 

cram = ['cat', 'bat', 'rat', 'elephant']
#chances the info inside value 2 
cram[1] = 'asdawasdwad'
#changes value 3 into value 2 
cram[2] = cram[1]
#changes the last value into info stated
cram[-1] = '12345678976543'
print(cram)

#Removing values from lists with del statements 

hram = ['cat', 'bat', 'rat', 'elephant']
#This deletes value 3 in hram variable 
del hram[2]
print(hram)
