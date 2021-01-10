### Basic Blockchain

#### Block class

`calc_hash` - O(1)

This still looks like constant time to me, I don't see anything that suggests that we are going to be doing anything with
the hash that needs to interate over each element in the data. Its definitely possible that the sha hashing algorithm grows
with the size of the data, but my research suggested that the most likely answer is constant time. Either way, it is probably
most accurate to say that `calc_hash` grows with whatever time complexity of the share hashing you choose. 

#### BlockChain class

`append` - O(1)

We create a new block (which this explanation assumes takes O(1)) and then append it to the chain using constant instructions. 
This is because we keep a reference to the `tail` of the node where we will be appending the block. I think in this case it
makes sense to keep the `tail` reference around otherwise we have to walk the entire block before we can add a single node, which
could get quite costly.
