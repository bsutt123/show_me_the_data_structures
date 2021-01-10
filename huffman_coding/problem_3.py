import sys
import heapq


class HuffNode:
    def __init__(self):
        self.left = None;
        self.right = None;
        self.char = None;
        self.frequency = None;

    def __lt__(self, other):
        if self.frequency is not other.frequency:
            return self.frequency < other.frequency
        elif self.char is not None and other.char is not None:
            return self.char < other.char
        elif self.char is not None:
            return True
        elif other.char is not None:
            return False
        else:
            return True



def get_letter_frequency(input_string):
    freq_counts = {}
    for char in input_string:
        if char in freq_counts:
            freq_counts[char] += 1
        else:
            freq_counts[char] = 1

    return freq_counts


def huffman_char_encodings(path, node, encodings):
    # Is this still necessary
    if node.char is not None:
        if path == "":
            return encodings

        encodings[node.char] = path
        return encodings

    if node.left is not None:
        encodings = huffman_char_encodings(path + "0", node.left, encodings)
    if node.right is not None:
        encodings = huffman_char_encodings(path + "1", node.right, encodings)

    return encodings


def huffman_encoding(data):
    heap = []

    frequencies = get_letter_frequency(data)

    for key in frequencies:
        node = HuffNode()
        node.char = key
        frequency = frequencies[key]
        node.frequency = frequency
        heapq.heappush(heap, node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        internal_node = HuffNode()
        internal_node.frequency = node1.frequency + node2.frequency
        internal_node.left = node1
        internal_node.right = node2

        heapq.heappush(heap, internal_node)

    # deal with special case of empty string
    if len(heap) == 0:
        fake_node = HuffNode()
        empty_node = HuffNode()
        empty_node.char = ""
        empty_node.freq = 1
        fake_node.right = empty_node

        return ["1", fake_node]

    # deal with special case of string with 1 char
    elif len(heap) == 1:
        fake_node = HuffNode()
        fake_node.right = heap[0]
        t = fake_node

    else:
        t = heap[0]

    encodings = huffman_char_encodings("", t, {})

    output = ""
    for char in data:
        output += encodings[char]

    return [output, t]


def huffman_decoding(data, tree):
    current_node = tree
    decoded_string = ""

    for datum in data:
        if datum == "1":
            current_node = current_node.right
        else:
            current_node = current_node.left

        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = tree

    return decoded_string


codes = {}

sentence_1 = "A great day for birds of a feather to flock together"
sentence_2 = "AAAAAAAAAA"
sentence_3 = ""

print("The size of the sentence_1 is: {}\n".format(sys.getsizeof(sentence_1)))
print("The size of the sentence_2 is: {}\n".format(sys.getsizeof(sentence_2)))
print("The size of the sentence_3 is: {}\n".format(sys.getsizeof(sentence_3)))

print("The content of the sentence 1 is: {}\n".format(sentence_1))
print("The content of the sentence 2 is: {}\n".format(sentence_2))
print("The content of the sentence 3 is: {}\n".format(sentence_3))

encoded_data_1, tree_1 = huffman_encoding(sentence_1)
encoded_data_2, tree_2 = huffman_encoding(sentence_2)
encoded_data_3, tree_3 = huffman_encoding(sentence_3)

print("The size of the encoded sentence 1 is: {}\n".format(sys.getsizeof(int(encoded_data_1, base=2))))
print("The size of the encoded sentence 2 is: {}\n".format(sys.getsizeof(int(encoded_data_2, base=2))))
print("The size of the encoded sentence 3 is: {}\n".format(sys.getsizeof(int(encoded_data_3, base=2))))

print("The content of the encoded sentence 1 is: {}\n".format(encoded_data_1))
print("The content of the encoded sentence 2 is: {}\n".format(encoded_data_2))
print("The content of the encoded sentence 3 is: {}\n".format(encoded_data_3))

decoded_data_1 = huffman_decoding(encoded_data_1, tree_1)
decoded_data_2 = huffman_decoding(encoded_data_2, tree_2)
decoded_data_3 = huffman_decoding(encoded_data_3, tree_3)

print("The size of the decoded sentence 1 is: {}\n".format(sys.getsizeof(decoded_data_1)))
print("The size of the decoded sentence 2 is: {}\n".format(sys.getsizeof(decoded_data_2)))
print("The size of the decoded sentence 3 is: {}\n".format(sys.getsizeof(decoded_data_3)))

print("The content of the decoded sentence 1 is: {}\n".format(decoded_data_1))
print("The content of the decoded sentence 2 is: {}\n".format(decoded_data_2))
print("The content of the decoded sentence 3 is: {}\n".format(decoded_data_3))
