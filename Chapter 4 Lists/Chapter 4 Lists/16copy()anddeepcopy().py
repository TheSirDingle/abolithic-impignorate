#Aaron Stockman

#imports many of the different copy functions
import copy 

#This copies the list from spam into cheese, then changes index 1 into 42
spam = ['A', 'B', 'C', 'D']
#regular copy function
chess = copy.copy(spam)
chess[1] = 42
print(spam)
print(chess)

#deepcopy() is used if the list you need to copy contains list of its own
#copy.deepcopy() is the function

damn = [1,2,3,4]
tram = [5,6,7,8]
yram = [9,10,11,12]
gram = [13,14,15,16]

hram = [damn, tram, yram, gram]
print(hram)
#copies the list and the lists inside the list
rest = copy.deepcopy(hram)
#changes list 2 to 42
rest[1] = 42
print(rest)