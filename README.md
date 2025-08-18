# FileSortersCSC318Final
A collection of python files that when run, will sort files according to the users preferences.

This is part of my final project for CSC318: Software Engineering Principles, by Pr. Tony Hinton

Functions:
SortByType - Sorts files by their extension type (e.g. '.png', '.jpg', '.webp')
SortAlphabetical - Sorts file alphabetically, if the file begins with a number then that file will go before the lettered files (0 - 9, a - z)
SortByDate - Sorts files by the date they were created, this file will put files into folders based on the month and year they were created

libraries used:
os
shutil
pathlib
datetime

Functionality/How To Use:
All of these files function similarly and have a defined structure to them (with some exceptions we will go over after). The files first import necessary libraries to function. Then you specify which directory you want sorted. To do this you must right click the file and choose "Copy Location". This is all you need to do with the file itself. Lastly, you will open the terminal and type "python (name of the file you want to run, e.g. SortByType)" and hit the enter button.

Exceptions:
The SortByType file works a little bit differently than the rest and has another piece of code you can add to for more functionality. There is a dictionary created within the file for making folders to add the different extension types to. The code looks like this:
extension_to_folder = {
    '.png': 'png',
    '.jpg': 'jpg',
    '.webp': 'webp'
}
You can add to this list by first typing in the name of the extension on the left, followed by a colon (:) and then type in the name of the folder to be put into on the right. This program is very simple and only includes some image formats for a demo, but you can add any extension you like to the file.
