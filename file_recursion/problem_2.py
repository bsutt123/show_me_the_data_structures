## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.exists(path):
        return []

    matched_files_from_dir = []

    directory_list = os.listdir(path)

    if len(directory_list) == 0:
        return matched_files_from_dir

    for item in directory_list:
        item_path = path + "/" + item
        if not os.path.exists(item_path):
            next
        elif os.path.isfile(item_path):
            if item.endswith(suffix):
                matched_files_from_dir += [item]
        elif os.path.isdir(item_path):
            matched_files_from_dir += find_files(suffix, item_path)

    return matched_files_from_dir


print(find_files(".c", "."))                            # returns ['b.c', 't1.c', 'a.c', 'a.c']
print(find_files("something that doesn't exist", "."))  # returns []
print(find_files("", "./subdir1/subdir"))               # returns [], no folder exists