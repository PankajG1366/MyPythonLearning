import random, os

# Define a clear screen function based on the guest OS type
def screen_clear():
    if os.name == 'posix': # for mac and linux os.name is 'posix'
        _ = os.system('clear')
    else:
        _ = os.system('cls') # for windows os.name is 'nt'

# Call the above defined function for clearing the screen
screen_clear()

secret = random.randint(1,20)
print("I am thinking of a number between 1 and 20")
print("You have 6 chances to make the guess of my number :)")

for i in range(1, 7):
    print("Guess the number:")
    guess = int(input())

    if guess < secret:
        print("Your guess is too low :(")
        print("You have " + str(int(6 - int(i))) + " guesses left")
        print()
    elif guess > secret:
        print("Your guess is too high :(")
        print("You have " + str(int(6 - int(i))) + " guesses left")
        print()
    else:
        break

if guess == secret:
    print("You have guessed the correct number in " +  str(i) + " guesses :)")
else:
    print("Chances over. My guessed number was " + str(secret) + ":)" )

