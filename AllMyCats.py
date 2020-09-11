import os

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

screen_clear()

catNames = []

while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')

    name = input()

    if name == '':
        break
    catNames = catNames + [name] ## This is concatenation of list so var 'name' is in square brackets

print('Cat names are:')
for names in catNames:
    print(' ' + names)