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
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
