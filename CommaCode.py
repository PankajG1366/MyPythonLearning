import os

# Define a clear screen function based on the guest OS type
def screen_clear():
    if os.name == 'posix': # for mac and linux os.name is 'posix'
        _ = os.system('clear')
    else:
        _ = os.system('cls') # for windows os.name is 'nt'

# Call the above defined function for clearing the screen
screen_clear()

mylist = []
while True:
    print("Enter the " + str(len(mylist) + 1) + " values to be stored in list" +
          "(Or enter nothing to stop.):")
    name = input()

    if name == '':
        break

    mylist = mylist + [name]

for names in mylist[:-2]:
    print(names, end=", ")
print(mylist[-2] + ' and ' + mylist[-1])

