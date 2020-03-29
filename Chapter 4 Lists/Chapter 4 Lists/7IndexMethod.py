#method is the same thing as a function, except it's a called on value
#index() allows you to check the what index a certain value inside a list is

spam=['hello', 'hi', 'howdy', 'heyas']
#outputs the index of the value hello inside list spam. 0 btw
print(spam.index('hello'))
print(spam.index('heyas'))

#this will cause a value error, saying that it's not in the list
"""
spam.index('howdy howdy howdy')
"""

#with duplicate values it outputs the first index, and disregards the second index
tram = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(tram.index('Pooka'))
