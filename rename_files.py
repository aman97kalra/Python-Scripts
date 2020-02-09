### Script to rename all the files in  a folder with a name of your choice. 
### Requirement : I needed a script to rename all the subtitle files of an anime series according to the episode number.


# provides functions for interacting with OS
import os

def rename():
        #path should be absolute and without wildcard characters
    folderPath = '/Users/Aman.Kalra/Desktop/WellDyne Images'
    items = os.listdir( folderPath )
    i = 0
    for filename in items:
        print( filename )
        oldName =  folderPath + '/' + filename
        newName = folderPath + '/' + "Image " + str(i) + '.png'
        os.rename( oldName , newName)

# this part is included for reusability of this file as a part of some another project
if __name__ == "__main__":
    rename()
