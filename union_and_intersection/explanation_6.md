### Union and Intersection

#### LinkedList class

`append` - O(1)

I chose to rewrite this to keep a reference to the tail around. This meant that it was possible to append to the end of
the linked list in constant time rather than in O(n) time, which I found preferable. I know that our focus was the union
and intersection function rather than building the linked list but I still felt better about it being constant.

#### functions

`union` - O(n)

For the union, we use a dictionary with hash keys to keep track of elements already added to the union set. Because we are
able to check if any of the nodes values have already been added to the list in constant time, I expect to have to execute
constant instructions for each element in the list, leading to a time complexity of O(n) where `n` is the addition of the
size of the 2 lists.

`intersection` - O(n)

This one is similar to `union` but with slightly higher space complexity, as we need to have 2 dictionary to track the elements
that are in each list separately. For list 1, we iterate through the list and add each element to the dictionary once. After
that dictionary is built, we iterate through the second list. If we don't already have that value in the dictionary and the
value is also in the dictionary for list 1, we append it to the intersection list. All of these instructions happen in constant
time, so the final time complexity is `O(n)` with the addition of the size of the 2 lists.

