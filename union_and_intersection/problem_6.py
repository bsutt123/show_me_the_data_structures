class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedListInterator:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.current_node = linked_list.head

    def __next__(self):
        if self.current_node is not None:
            returned_node = self.current_node
            self.current_node = self.current_node.next
            return returned_node

        raise StopIteration


class LinkedList:
    def __init__(self, list = []):
        self.head = None
        self.tail = None
        self.size = 0

        for item in list:
            self.append(item)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        return LinkedListInterator(self)

    def append(self, value):

        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node
        self.size += 1


def union(llist_1, llist_2):
    union_dict = {}
    union_list = []

    for node in llist_1:
        if node.value not in union_dict:
            union_dict[node.value] = True
            union_list.append(node.value)

    for node in llist_2:
        if node.value not in union_dict:
            union_dict[node.value] = True
            union_list.append(node.value)

    return union_list


def intersection(llist_1, llist_2):
    llist_1_dict = {}
    llist_2_dict = {}
    intersection_list = []

    for node in llist_1:
        if node.value not in llist_1_dict:
            llist_1_dict[node.value] = True

    for node in llist_2:
        if node.value not in llist_2_dict:
            llist_2_dict[node.value] = True
            if node.value in llist_1_dict:
                intersection_list.append(node.value)

    return intersection_list


# Test case 1

linked_list_1 = LinkedList([3, 2, 4, 35, 6, 65, 6, 4, 3, 21])
linked_list_2 = LinkedList([6, 32, 4, 9, 6, 1, 11, 21, 1])

print(union(linked_list_1, linked_list_2)) # returns [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print(intersection(linked_list_1, linked_list_2)) # returns [6, 4, 21]

# Test case 2

linked_list_3 = LinkedList([3, 2, 4, 35, 6, 65, 6, 4, 3, 23])
linked_list_4 = LinkedList([1, 7, 8, 9, 11, 21, 1])

print(union(linked_list_3, linked_list_4)) # returns [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
print(intersection(linked_list_3, linked_list_4)) # returns []

linked_list_5 = LinkedList([])
linked_list_6 = LinkedList([])

print(union(linked_list_5, linked_list_6)) # returns []
print(intersection(linked_list_5, linked_list_6)) # returns []

linked_list_7 = LinkedList([1,1,1,1,1,1,1,1,1,1])
linked_list_8 = LinkedList([2,2,2,2,2,2,2,2,2,2,2,2,2,2])

print(union(linked_list_7, linked_list_8)) # returns [1, 2]
print(intersection(linked_list_7, linked_list_8)) # returns []

linked_list_9 = LinkedList([0,1,2,3,4,5,6,7,8,9])
linked_list_10 = LinkedList([0,1,2,3,4,5,6,7,8,9])

print(union(linked_list_9, linked_list_10)) # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intersection(linked_list_9, linked_list_10)) # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
