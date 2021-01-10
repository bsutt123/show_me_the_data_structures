 ### Huffman Coding
 
#### Implementation

`get_letter_frequency`: O(n)

This is a simple counting function storing the count in a hash. The number of executions will grow linearly with string size
which is common with `for` loop functions

`huffman_char_encodings`: O(n)

This is how we build up the encodings for the tree. It uses a depth first search for the nodes on the tree with characters,
and the runtime will grow linearly with respect to the number of nodes in the tree.

`huffman_encoding`: O(n * log(n))

I am going to break this function down into its different parts, and the time complexity will be the largest time complexity.
Some of this is assumptions from the `heapq` algorithm, but I think that pythons implementation should be considered at least
average.

1. Get the letter frequencies: O(n) - dicussed in `get_letter_frequency` above
2. Build letter frequency heap: O(n * log(n)) - we build a node with a a frequency and a key, and then push it onto a heap.
Insertion into a min heap is likely a `O(log(n))` operation, as the expectation is that at worst you will need to make `log(n)`
swaps in order to reheapify the heap. Because each node in the heap and each insertion is a `log(n)` operation. I would expect
that the final time complexity be `O(n * log(n))`. In my research it seems like its possible with the right initial heap
structure to perform the heapification in `O(n)`, but this I think would require all the elements to be in the heap at the 
start and then heapify once, which I don't know if it is possible with `HuffNode`s rather than `int`s.

3. Build the tree from the heap: O(n * log(n)) - Very similar logic applies in this case. In this case we don't do quite as many
insertions, as we pop off 2 nodes for every 1 that we add back in, but the order of magintude that it grows is still `O(n * log(n))`.

4. Get char encodings - O(n) - dicussed in the `huffman_char_encodings` function time complexity analysis.

5. Build encoded string - O(n) - pretty straightforward replacement one for one of char with encoded ones and zeros, expectation
is that we excute this part of the function in linear time.

This leads to a final time complexity of `O(n * log(n))`, as this was the most expensive operation in the process of building
the Huffman encoded string and tree.

`huffman_decoding` - O(n)

Compared to the encoding, decoding is actually quite simple. For each element in the encoded string (n) we will execute a constant
number of operations to identify that as either then end of the encoding and replace it with a char, or keep walking
the tree until we get to a char. Executing constant instructions for each element in the list leads to O(n) time complexity.







asdfasdf
