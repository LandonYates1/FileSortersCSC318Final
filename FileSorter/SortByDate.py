import os
import shutil
import datetime # this library is specific to this file as it finds the date of the file
from pathlib import Path

path = Path(r"/home/landon/Documents/Sort/SortByDate") # path goes here

# this is the function that finds and sorts the files
for item in path.iterdir():
    if item.is_file():
        creation_time = os.path.getctime(item)
        creation_date = datetime.datetime.fromtimestamp(creation_time)

        # creates the destination folder and gives it a name based on the year/month format
        folder_date = creation_date.strftime('%Y-%m')

        # defines the destination path and creates one if it doesn't already exist
        destination_folder = path / folder_date
        destination_folder.mkdir(exist_ok=True)
        print(f"Created folder: {destination_folder}")

        # moves the file to the new folder and prints completion message
        shutil.move(str(item), str(destination_folder / item.name))
        print(f"Moved '{item.name}' to the '{folder_date}' folder.")
