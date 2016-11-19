#=========================================================#
# Python 2.7.12                                           #
#                                                         #
# Create code that will move .txt files from one folder   #
# to another with the click of a button.                  #
#                                                         #
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) #     
#                                                         #
#======================={nWc}=============================#

import shutil
import os

print ('\nWelcome to Python File Mover')

#Initial file move request:
def option():
    stop = True
    while stop:
        entre = raw_input('\nWould you like to move your .txt files to a different folder, y/n? ').lower()
        if entre == 'y':
            txtMover()
            redo()
            stop = False
        elif entre == 'n':
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
            option()
        

#File Mover:    
def txtMover():

    srcFolder = 'C:\\Users\\nicho\\Desktop\\Folder A\\'
    source = os.listdir(srcFolder)
    dstFolder = 'C:\\Users\\nicho\\Desktop\\Folder B\\'
    for files in source:
        if files.endswith('.txt'):
           shutil.move(os.path.join(srcFolder, files), os.path.join(dstFolder, files))
           print(dstFolder + files)

           
#Return to original folder?:
def redo():
    stop = True
    while stop:
        entre = raw_input('\nDo you wish to return the items back to the previous folder, y/n? ').lower()
        if entre == 'y':
            txtReMover()
            redoTwo()
            stop = False
        elif entre == 'n':
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
            option()


#Re-Return folders...?:
def redoTwo():
    stop = True
    while stop:
        entre = raw_input('\nDo you wish to return the items back to the previous folder, y/n? ').lower()
        if entre == 'y':
            txtMover()
            redo()
            stop = False
        elif entre == 'n':
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO'...")
            option()

            
# File Mover Backerer:    
def txtReMover():

    srcFolder = 'C:\\Users\\nicho\\Desktop\\Folder B\\'
    source = os.listdir(srcFolder)
    dstFolder = 'C:\\Users\\nicho\\Desktop\\Folder A\\'
    for files in source:
        if files.endswith('.txt'):
           shutil.move(os.path.join(srcFolder, files), os.path.join(dstFolder, files))
           print(dstFolder + files)



option()



if __name__ == "__main__":
    option()




