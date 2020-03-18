#Aaron Stockman

#this programs uses list inside of for loops

#prints numbers 0-19
for i in range(20):
    print(i)

#prints whatever is in the list
for t in [0,1,2,3]:
    print(t)

#creates a for loop that outputs index # and what supplies is in that index #
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' +supplies[i])

"""
Using range(len(supplies)) is useful because it can acess the index (as the variable i)
and the value at that index (as supplies[i]). range(len(supplies)) will also iterate through
every index in supplies. 
"""