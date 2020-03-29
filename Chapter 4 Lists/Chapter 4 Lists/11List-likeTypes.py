#strings can also be tampered with like list, but not changed

name = 'Zophie'
#prints letter Z of Zophie 
print(name[0])
print(name[2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('Z' not in name)

for i in name:
    print('* * * ' + i + ' * * *')
