# Python 2.7.12
# 
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com)
#
# Python Drill Math Game - Tech Academy
#
#----------------------------------------------------------------------

# x = integer variable
# y = float variable

# Start of program
def start(stringage=""):
    stringage = intro(stringage)
    #math_operations()

# Intro while loop to decide whether or not to play game
def intro(stringage=""):
    stop = True
    while stop:
        entre = raw_input("\nWould you like to play a simple math game? y/n: ").lower()
        if entre == "y":
            stop = False
            welcomeage(stringage)
        elif entre == "n":
            entre_deux = raw_input("\nAre you sure? y/n: ")
            stop = True
            while stop:
                if entre_deux == "y":
                    stop = False
                    exit()
                elif entre_deux == "n":
                    intro(stringage = "")
                else:
                    print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
    
    

# Welcome function and loop - name and number entry
def welcomeage(stringage):

    if stringage != "":
        print("\nWelcome Back, {}!".format(stringage))
    else:
        stop = True
        while stop:
            if stringage == "":
                # 2. Assign a string to a variable stringage
                stringage = raw_input("\nPlease enter your name: ").title()
                if stringage != "":
                    print("\nWelcome to a simple math program, {}!".format(stringage))
                    print("\nIn this program, you will be asked to enter two numbers. \nYou can then carry out several mathematical operations using the numbers.")
                    # 1. Assign an integer to a variable
                    x = raw_input("\nPlease enter a whole number (ex. 12, 345, 67, etc.): ")
                    # 3. Assign a float to a variable
                    y = raw_input("\nPlease enter a number with a decimal point (ex. 12.3, 4.56, 789.0, etc.): ")
                    stop = False
    math_operations(x,y,stringage)
    return (x,y,stringage)


# Math function and loop to decide what operation to use
def math_operations(x,y,stringage):
    stop = True
    while stop:
        mathOps = raw_input("\nWhat operation would you like to perform with your numbers? (+, -, *, /, %): ")
        if mathOps == "+":
            print("\nThe sum of your numbers is {}".format(float(x)+float(y)))
            stop = False
            replay(x,y,stringage)
        elif mathOps == "-":
            print("\nThe difference of your numbers is {}".format(float(x)-float(y)))
            stop = False
            replay(x,y,stringage)
        elif mathOps == "*":
            print("\nThe product of your numbers is {}".format(float(x)*float(y)))
            stop = False
            replay(x,y,stringage)
        elif mathOps == "/":
            print("\nThe quotient of your numbers is {}".format(float(x)/float(y)))
            stop = False
            replay(x,y,stringage)
        elif mathOps == "%":
            print("\nThe remainder of your first number divided by your second number is {}".format(float(x)%float(y)))
            stop = False
            replay(x,y,stringage)
        else:
            print("\nPlease use one of the following operators only: (+, -, *, /, %)... ")
    return (x,y,stringage)   
            

# Function and loop to decide to replay game
def replay(x,y,stringage):
    stop = True
    while stop:
        choose = raw_input("\nWould you like to perform any additional operations on your numbers? y/n: ").lower()
        if choose == "y":
            stop = False
            newOps(x,y,stringage)
        elif choose == "n":
            drillChoice = raw_input("\nThank you for playing! \nWould you like to see the required coding drill output? y/n: ").lower()
            stop = True
            while stop:    
                if drillChoice == "y":
                    stop = False
                    drill_code()
                elif drillChoice == "n":
                    print("\n\nSorry, we're going there anyway...it will be (mostly) painless.\n\n")
                    stop = False
                    drill_code()
                else:
                    print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
        


# function to replay while retaining name and numbers for operations
def newOps(x,y,stringage):
    x = x
    y = y
    math_operations(x,y,stringage)


# Drill code
def drill_code():
    # 1. Assign an integer to a variable
    int_variable = 6


    # 2. Assign a string to a variable
    string_variable = "This is a string."


    # 3. Assign a float to a variable
    float_variable = 3.14

    print("================================================================================")
    # 4. Use the print f'n and .format() notation to print out assigned variable
    print("\nThe assigned variables are...\ninteger: {},\nstring: \"{}\", \nand float: {}\n".format(int_variable,string_variable,float_variable))


    # 5. Use each operator (+,-,*,/,+=,=,%)
    x = 12
    y = 5.3
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("x plus y is equal to {}".format(x+y))
    print("x minus y is equal to {}".format(x-y))
    print("x times y is equal to {}".format(x*y))
    print("x divided by y is equal to {}".format(float(x)/float(y)))
    print("The remainder of x divided by y is {}".format(float(x)%float(y)))
    x+=y
    print("The sum of x and y returns a new value for x, which is now {}".format(x))

    # 6. Use of logical operators: and, or, not
        # and:
    if (2 == 2) and (2 + 2 > 2):
        print("\nThe logical operator 'and' returns true!")
    else:
        print("\nThe logical operator 'and' returns false!")

       # or:
    x = 25
    y = 250
    if x > 30 or y < 1000:
        print("\nThe logical operator 'or' returns true!\n")

        # not:
    if not True:
        print("The logical operator 'not' returns 1")
    elif not(2 + 2 ==3):
        print("The logical operator 'not' returns 2")
    else:
        print("The logical operator 'not' returns 3")


    #7. Use of conditional statements: if, else, elif
    x = 10
    if x == 5:
        print("\nIf statement returns 5\n")
    elif x == 11:
        print("\nElif statement returns 11\n")
    else:
        print("\nElse statement returns x = 10\n")
    

    #8. Use of a while loop
    i = 5
    while True:
        print(i)
        i = i -1
        if i <= 0:
            break

    
    print("\n")


    #9. Use of a for loop
    for x in range(0,7):
        print(x)

    print("\n")

    #10. Create a list and iterate through the list w/for loop
    python_drill_list = ["Item One", "Item Two", "Item Three", "Item Four", "Item Five"]

    for item in python_drill_list:
        print item

    print("\n")


    #11. Create a tuple and iterate through the tuple w/for loop
    python_drill_tuple = ("These", "are", "the", "tuple", "bits")

    for bit in python_drill_tuple:
        print bit

    print("\n")

    #12. Define a function that returns a string variable
    def string_function(str):                             
        print str
        return()

    #13. Call the function and print result to the shell
    string_function("This is the result of the called string function.")
    



if __name__ == "__main__":
    start()
