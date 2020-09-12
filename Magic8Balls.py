import random, os

# Define a clear screen function based on the guest OS type
def screen_clear():
    if os.name == 'posix': # for mac and linux os.name is 'posix'
        _ = os.system('clear')
    else:
        _ = os.system('cls') # for windows os.name is 'nt'

# Call the above defined function for clearing the screen
screen_clear()

messages = [ 'It is certain',
             'It is decidedly so',
             'Yes definitely',
             'Reply hazy try again',
             'Ask again later',
             'Concentrate and ask again',
             'My reply is no',
             'Outlook not so good',
             'Very doubtful'
]

print(messages[random.randint(0, len(messages) - 1 )])