import random 

"""
Return statement has the return keyword, the value/expression that 
function should return
"""

#defines getAnswer function with the answerNumber parameter 
#skips over the code in it because function is being defined 
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

#random.radint is called for integers 1-9, and is set to r as the argument
r = random.randint(1,9)
#r is then set as a parameter in getAnswer, which means r is stored in the parameter answerNumber
fortune = getAnswer(r)
#prints whatever string value it get from the function
print(fortune)

#note: you can also do print(getAnswer(random.randint(1,9)))
