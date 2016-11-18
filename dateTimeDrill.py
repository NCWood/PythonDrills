#=========================================================#
# Python 2.7.12                                           #
#                                                         #
# Create code that will use the current time in Portland  #
# to find out if offices in NYC and London are open.      #
#                                                         #
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) #                                                     #
#                                                         #
#======================={nWc}=============================#

import datetime
from datetime import datetime, timedelta

pdxTime = datetime.now()
nycTime = datetime.now() + timedelta(hours = 3)
ukTime = datetime.now() + timedelta(hours = 8)

print ('\nThe current date and time in Portland, Oregon is {}.'.format(pdxTime))

# Start of program:
def checkOpen():
    stop = True
    while stop:
        entre = raw_input("\nWhich branch would you like to verify open/closed status, New York or London?").lower()
        if entre == 'new york':
            nycBranch()
        elif entre == 'london':
            ukBranch()
        else:
            print("\nPlease enter either 'New York' or 'London'.  Thank you.")            

def nycBranch():
    if nycTime.hour >= 9 and nycTime.hour < 21:
        print ('\nThe New York office is currently open.')
        anotherBranch()
    else:
        print ('\nThe New York office is currently closed.')
        anotherBranch()

def ukBranch():
    if ukTime.hour >= 9 and ukTime.hour < 21:
        print ('\nThe London office is currently open.')
        anotherBranch()
    else:
        print ('\nThe London office is currently closed.')
        anotherBranch()

def anotherBranch():
    choose = raw_input("\nWould you like to check the status of another branch? y/n: ").lower()
    if choose == "y":
        stop = False
        checkOpen()
    elif choose == "n":
        print ("\nThank you, Have a nice day.")
        closeApp()
    else:
        print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
        anotherBranch()

def closeApp():
    exit()


checkOpen()



if __name__ == "__main__":
    checkOpen()

