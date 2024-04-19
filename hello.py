#Making my first python program which takes in a name as input from the user

import sys #Import sys module to take in command line arguments

if len(sys.argv) > 1: #Check for arguments as input
    name = sys.argv[1] #Get the first argument after script name
    print(f"Hello, {name}!") #Greet the user
else:
    print("Hello stranger!")
    



