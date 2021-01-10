"""
Requirements:

Fast Lookups: O(1)
Suggested Structure: HashMap/Python Dictionary
Why: About the only way to get constant time lookups is going to be an array or a hasp map. In this case we
don't just have indices, so it will _probably_ be best to store the value as the key in the hash map.

Fast insertion and deletion: O(1)
Suggested Structure: Doubly Linked List
Why: We need to be able to remove the "least recently used" element and insert a new one in constant time. That sounds
to me like a double linked list that lets me insert elements at the head of the list and remove from the tail. Or in the
case of a cache hit move that element back to the front from where it is in the cache
"""


class DoubleLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

            if self.length == self.capacity:
                return self.remove_tail()
            else:
                self.length += 1
                return None

    def remove_tail(self):
        tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        return tail

    def swap_to_head(self, node):
        if self.head == node:
            return
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_map = {}
        self.cache_list = DoubleLinkedList(capacity)

    def get(self, key):
        if key in self.cache_map:
            cache_node = self.cache_map[key]
            self.cache_list.swap_to_head(cache_node)
            return cache_node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache_map and value == self.cache_map[key].value:
            self.cache_list.swap_to_head(self.cache_map[key])
        else:
            node = DoubleLinkedNode(key, value)
            self.cache_map[key] = node
            removed_node = self.cache_list.insert(node)
            if removed_node:
                del self.cache_map[removed_node.key]


our_cache = LruCache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))       #returns -1 because it should have fallen out

