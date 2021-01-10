## LRU Cache

### Requirements:

#### Fast Lookups: O(1)
Suggested Structure: HashMap/Python Dictionary
Why: About the only way to get constant time lookups is going to be an array or a hasp map. In this case we
don't just have indices, so it will _probably_ be best to store the value as the key in the hash map.

#### Fast insertion and deletion: O(1)
Suggested Structure: Doubly Linked List
Why: We need to be able to remove the "least recently used" element and insert a new one in constant time. That sounds 
to me like a double linked list that lets me insert elements at the head of the list and remove from the tail. Or in the
case of a cache hit move that element back to the front from where it is in the cache

### Implmentation

Double Linked Node: This is pretty standard. I stored both the key and the value so that removal from the dictionary
would be simpler

Double Linked List: Really nothing crazy here either. `swap_to_head` is useful because we need to move nodes from where
they are in the list to the front if they are used in the cache, but with a double linked list this leads to quite a bit of connection
breaking and reforming. Overally not wildly complex operations but it does make the code a bit lengthier

In this case when inserting, it also _returns_ the node the was removed from the list. This help communicate back to the 
cache that is using it that it was deleted and should be removed from the dictionary.

LruCache: This is just the combination of the HashMap and the List. When getting a key, it checks if it is in the dict,
and swaps the node to the front if it exists, or returns -1.

for `set`, if the key is already in the list and is the same value, it just swaps it to the front. Otherwise, a new node
is created to hold the key value pair. The key is inserted in the map, the node is inserted into the list, and if a node
was removed from the list it is removed from the dict.


### Runtimes

#### DoubleLinkedList

`insert`: O(1)

Because we store the head of the list we can insert at the front in constant time. 

`remove_tail`: 0(1)

Because there is a reference to the tail it can be identified and removed in constant time

`swap_to_head`: O(1)

This function executes more lines of code, but they are still constant with respect to the size of the list because
the number of executions remains the same, as it doesn't take any more code to jump to the head and reform the connections
at the back of the list.

#### LruCache

`get`: O(1)

Using the HashMap for detection and the List for insertion and deletion means that this can happen in constant time

`set`: O(1)

Just like get, using the dual data structures for this implementation leads to the best of both worlds (fast access and
fast insertion) at the cost of memory space.
