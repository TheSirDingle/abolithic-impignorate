
#importing different modules 
#importing allows you to add a group of related modules to your program

#imports the random module which allows for randomized functions 
import random
#imports functions from system, os, and math library
import sys, os, math 

#prints a random 5 #'s between 0 and 10
for i in range (5):
    #random.randiant evaluates to a random integer value 
    print(random.randint(1,10))

for i in range (20):
    #exits the program early, in turn not executing the random 1,100
    sys.exit()
    print(random.randint(1,100))
