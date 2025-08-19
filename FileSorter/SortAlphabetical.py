import os
import shutil
from pathlib import Path

# defines your chosen path
path = Path(r"/home/landon/Documents/Sort/SortAlphabetical") # path goes here

# this is the function that finds and sorts the files
for item in path.iterdir():
    if item.is_file():
        # gets only the first character of the file and converts to lowercase, also defines the folder
        first_char = item.name[0].lower()

        # creates the destination folders
        destination_folder = path / first_char

        # creates the folder if it doesn't already exist
        if not destination_folder.exists():
            destination_folder.mkdir()
            print(f"Created folder: {destination_folder}")

        # defines the destination path
        destination_path = destination_folder / item.name

        # moves the file to the new folder and prints completion message
        shutil.move(str(item), str(destination_path))
        print(f"Moved '{item.name}' to the '{first_char}' folder.")

# import os
# import shutil
# from pathlib import Path
#
# path = r"/home/landon/Documents/Sort/SortAlphabetical"
#
# file_names = os.listdir(path)
#
# folder_names = path / first_char
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
#     if file_name.startswith('a'):
#             destination_path = os.path.join(path, 'a', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'a' folder.")
#     elif file_name.startswith('r'):
#             destination_path = os.path.join(path, 'r', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'r' folder.")
#     elif file_name.startswith('z'):
#             destination_path = os.path.join(path, 'z', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the 'z' folder.")
#     elif file_name.startswith('4'):
#             destination_path = os.path.join(path, '4', file_name)
#             shutil.move(source_path, destination_path)
#             print(f"Moved '{file_name}' to the '4' folder.")
