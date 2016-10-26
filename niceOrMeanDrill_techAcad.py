# Python 2.7.12
#
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) & Tech Academy Tutorial
#
# Purpose: How to pass variables from function to function while
#          producing a functional game.
# function_name(variable) - means we pass in the variable
# return variable - means we are returning the variable to the calling f'n

#------------------------------------------------------------------------------------------------
# def start():
#    print("Hello {}!".format(get_name()))
#
# def get_name():
#    name = raw_input("What is your name? ")
#    return name

'''def start ():
    f_name = "Sherlock"
    l_name = "Holmes"
    age = 45
    gender = "Male"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}.  I am a {} year old {}.".format(f_name,l_name,age,gender)) '''

#-------------------------------------------------------------------------------------------------

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    '''
        check if this is a new game or not:
        if it is new, get user's name
        if not new, thank player for playing again and continue with the game
    '''
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").title()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                    print("At the end of the game, your fate will be influenced by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation.\nWill you be nice or mean n/m: ").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger stares at you menacingly and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, you currently have({}, Nice) and ({}, Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    # scofe f'n is being passed the values stored w/in the3 variables
    if nice > 5: # if condition is valid, call win function passing in the variables for use
        win(nice,mean,name)
    if mean > 5: # if condition is valid,...
        lose(nice,mean,name)
    else:       # else, call nice_mean f'n ...
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you now live in a palace!".format(name))
    again(nice,mean,name) # Call again f'n and pass in our variables

def lose(nice,mean,name):
    print("\nToo bad, game over {}! \nYou live in a van down by the river,  wretched and alone!".format(name))
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you later, alligator!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # no name reset, as user is playing again
    start(nice,mean,name)

        




if __name__ == "__main__":
    start()












    
