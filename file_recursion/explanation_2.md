### File Recursion

#### Implementation

For the recursive function, we start by making sure the path exists, and then asking for all the items in the directory.
Iterating over each item, we identify any files, and check for the suffix, noting a match. For directories, we recursively
call the function for that directory, searching for additional files that might match before finally returning all the matches
found. Pretty standard recursion, though the lack of Proper Tail Recursion in python does mean that there are some limits
to the depth of the file structure that this can look through

#### Runtime Analysis

`find_files`: O(n)

I would expect this to run in linear time with respect to the number of files and folders searched. More precisely if there
are `n` files and `m` folders to search through you would expect O(n+m), but what that really boils down to is linear time.
The number of executions to identify a single file is constant, and the number of instructions to process a folder is constant,
even if further processing on the files in the folder will be in linear time within that folder. 