""" 
program name: pseudonymns.py
objective: generate funny random nick names
"""

import sys, random 

# print welcome message:
print("Welcome to the Psych 'Sidekick Name Picker'")
print("A name just like Sean would pick for Gus:\n")
print("*"*40)

# load two list one contins first names other second/last names
first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'","Bob 'Stinkbug'")
last = ('Appleyard', 'Bigmeat', 'Bloominshine','Boogerbottom', 'Breedslovetrout')

while True:
    # randomly choose a name(string) from the first tuple
    firstName = random.choice(first)
    
    # randomly choose a name(string) from the last tuple
    lastName = random.choice(last)
    print("**************")
    print(">> {} {}".format(firstName,lastName), file=sys.stderr)
    print("**************")
    try_again = input("Do you wanna try again?\n[Yes] Enter to continue [No] n to quit: ")
    if try_again.lower() == "n":
        break
input = ("press enter to exit..")