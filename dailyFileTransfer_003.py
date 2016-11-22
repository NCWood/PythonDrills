#=========================================================#
# Python 2.7.12                                           #
#                                                         #
# Create code that will determine which files are new or  #
# recently edited and copy them to destination folder.    #
#                                                         #
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) #     
#                                                         #
#======================={nWc}=============================#

# module imports
import shutil
import os
from os import path
import datetime
from datetime import datetime, date, time, timedelta


# title
print ('Daily File Transfer\n')


# paths, etc...
dailyHold = 'C:\\Users\\nicho\\Desktop\\dailyHold\\'
homeOffice = 'C:\\Users\\nicho\\Desktop\\homeOffice\\'



# yesterday
aDayOld = datetime.now() - timedelta(hours = 24)
print ('\n')
#print (aDayOld)



#Initial file copy request:
def option():
    stop = True
    while stop:
        entre = raw_input('Would you like to copy today\'s files to the Home Office folder, y/n? ').lower()
        if entre == 'y':
            dailyTransfer()
            stop = False
            print ('\nFile copy complete!')
            outro()
        elif entre == 'n':
            print ('\nGoodbye')
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
            option()
        
# Daily Transfer - will copy files created or modified within the last 24 hours
def dailyTransfer():
    for root, dirs, files in os.walk(dailyHold):
        for txtfile in files:
            path = os.path.join(root, txtfile)
            st = os.stat(path)
            mtime = datetime.fromtimestamp(st.st_mtime)
            ctime = datetime.fromtimestamp(st.st_ctime)
            if mtime > aDayOld and txtfile.endswith('.txt'):
                shutil.copy(os.path.join(dailyHold, txtfile), os.path.join(homeOffice, txtfile))
            elif ctime > aDayOld and txtfile.endswith('.txt'): 
                shutil.copy(os.path.join(dailyHold, txtfile), os.path.join(homeOffice, txtfile))

# Exit Options
def outro():
    stop = True
    while stop:
        entre = raw_input('\nWould you like to exit the program, y/n? ').lower()
        if entre == 'y':
            print ('\nGoodbye')
            exit()
        elif entre == 'n':
            print ('\nGoodbye')
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
            outro()






if __name__ == "__main__":
    option()



    

