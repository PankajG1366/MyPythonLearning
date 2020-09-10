import os

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

screen_clear()

def collatzseq(number):

    num = int(number)

    if (num % 2) == 0:
        print(str(num // 2))
        r = int(num // 2)
        return r
    elif (num % 2) == 1:
        print(str(num * 3 + 1))
        r = int(num * 3 + 1)
        return r

print("Enter number:")
mynum = input()
try:
    n = int(mynum)
    while n != 1:
        n = collatzseq(n)
except ValueError:
    print("Please enter an integer")






