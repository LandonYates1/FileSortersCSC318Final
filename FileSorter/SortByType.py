# importing libraries
import shutil
from pathlib import Path

# defines your chosen path
path = Path(r"/home/landon/Documents/Sort/SortByType") # path goes here

# making  dictionary for making the folders based on each file extension type
extension_to_folder = {
    '.png': 'png',
    '.jpg': 'jpg',
    '.webp': 'webp'
}

# this is the function that finds and sorts the files
for item in path.iterdir(): # repeats process
    if item.is_file(): # gets the file extension and sets all the text to lowercase
        extension = item.suffix.lower() # this makes it easier for the file sorter to read

        # puts the files in their respective folders based on extension type and defines the folder
        if extension in extension_to_folder:
            folder_name = extension_to_folder[extension]
        else:
            folder_name = 'Other'  # safety net for any extension not specified in the dictionary

        # creates the path for the destination folder and destination file
        destination_folder = path / folder_name
        destination_file = destination_folder / item.name

        # creates the folder if it doesn't already exist
        if not destination_folder.exists():
            destination_folder.mkdir()
            print(f"Created folder: {destination_folder}")

        # this moves the file to its destination folder and prints completion message
        shutil.move(str(item), str(destination_file))
        print(f"Moved '{item.name}' to the '{folder_name}' folder.")

# import os
# import shutil
# from pathlib import Path
#
# path = r"/home/landon/Documents/Sort/SortByType"
#
# file_names = os.listdir(path)
#
#
# folder_names = ['png', 'jpg', 'webp']
#
# for folder_name in folder_names:
#     folder_path = os.path.join(path, folder_name)
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#         print(f"Created folder: {folder_path}")
#
# for file_name in file_names:
#     source_path = os.path.join(path, file_name)
#
#     # Make sure we're only moving files, not directories
#     if os.path.isfile(source_path):
#         # Use a series of if/elif/else statements to sort files
#         if file_name.endswith('.png'):
#             destination_path = os.path.join(path, 'png', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'png' folder.")
#         elif file_name.endswith('.jpg'):
#             destination_path = os.path.join(path, 'jpg', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'jpg' folder.")
#         elif file_name.endswith('.webp'):
#             destination_path = os.path.join(path, 'webp', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'webp' folder.")
#         else:
#             # If the file type doesn't match any of the above, move it to 'other'
#             destination_path = os.path.join(path, 'other', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'other' folder.")
