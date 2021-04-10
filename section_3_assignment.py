# 1) Create a list of names and use a for loop to output the length of each name (len() ).
# COMPLETED
# 2) Add an if  check inside the loop to only output names longer than 5 characters.
# COMPLETED
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.

# 4) Use a while  loop to empty the list of names (via pop() )

# initialize list to store names
names = []

# function definitions
def print_name_length():
    """ Prints the length of each name that is present in the list.  Uses global names list."""
    
    for index in range(len(names)):
        name = names[index]
        if len(name)> 5:
            print(name + ' is ' + str(len(name)) + ' characters long')

# Use a while loop to collect names from user
smash_it = True

while smash_it:
    print('1: Enter a name')
    print('2: Output Names')
    print('3: Output length of each Name')
    print('q: Quit')

    user_choice = str(input())
    if user_choice == '1':
        print('Enter a name ')
        name = input()
        names.append(name)
    elif user_choice == '2':
        print(names)    
    elif user_choice == '3':
        print_name_length()
    elif user_choice == 'q':
        print('User chose to exit.')
        smash_it = False
    else:
        print('Choose a valid option')