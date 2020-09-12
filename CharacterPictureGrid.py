import os

# Define a clear screen function based on the guest OS type
def screen_clear():
    if os.name == 'posix': # for mac and linux os.name is 'posix'
        _ = os.system('clear')
    else:
        _ = os.system('cls') # for windows os.name is 'nt'

# Call the above defined function for clearing the screen
screen_clear()

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

for i in range(0,len(grid[0])):
    for j in range(0,len(grid)):
        print(grid[j][i], end='')
    print()
