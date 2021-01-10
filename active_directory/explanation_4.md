### Active Directory

`is_user_in_group`: O(n)

I changed the implementation slighty for group so that in addition to keeping a list of the users, it also kept a dictionary
of the user_ids that were in the group. This means that its possible to check if a user is a group in constant time rather
than linear time. 

For each group we have to check if the user is in the group happening on O(1), and then also check any sub_groups if the user
is not in the current group. As we will execute constant instruction O(1) for each subgroup, I would expect that the time
complexity of the function would be O(n) growing linearly with the size of the group.

If I had not chosen to store the user ids in a dictionary as well, then I would still expect the time complexity to be O(n).
We would have needed to make an addition O(m) execution to check the group for a user within each group. This might lead to a 
time complexity described as O(n + m) where `n` and `m` are the total number of groups and users in the tree, but 2 linearly growing
functions together still have a final time complexity of O(n) because we do not have any kind of nested for loops inside 
the function.

I would call `O(n)` efficient lookups. If O(1) was desired, then I think that there would need to be a different structure entirely,
something focused on storing the user_ids in a hash with references to the groups that they are in rather than having groups
be the keepers of the information about each of the users in the group.