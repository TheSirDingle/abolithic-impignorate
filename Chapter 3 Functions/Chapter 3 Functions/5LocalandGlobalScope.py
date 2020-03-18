#aaron stockman

def spam():
    #this is a local statement since it's inside a function 
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
  


spam()

#this is a global statement since it's not inside a defined function
eggs = "global "


