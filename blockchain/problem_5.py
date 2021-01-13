import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.data + str(self.timestamp)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.root = None
        self.tail = None

    def append(self, data):
        if self.root is None:
            block = Block(datetime.datetime.now().timestamp(), data, None)
            self.root = block
            self.tail = block
            return

        block = Block(datetime.datetime.now(), data, self.tail.hash)
        self.tail.next = block
        self.tail = block

    def __str__(self):
        if self.root is None:
            return ""
        current_node = self.root
        string = ""
        while current_node.next is not None:
            string += f'data: {current_node.data}, prev_hash: {current_node.previous_hash}, hash: {current_node.hash}'
            string += " -> "
            current_node = current_node.next

        string += f'data: {current_node.data}, prev_hash: {current_node.previous_hash}, hash: {current_node.hash}'
        return string


chain1 = BlockChain()
chain2 = BlockChain()
chain3 = BlockChain()

chain1.append("somthing")
chain1.append("something else")
chain1.append("one last thing")

chain2.append("thesamething")
chain2.append("thesamething")
chain2.append("thesamething")


# I can't tell you exactly what these will look like but it will be roughly this

print(chain1)

# returns data: somthing, prev_hash: None, hash: 8ef0fbdd7478a8654251efe1791909cfc9f33f71b1427a3a4a85c3f1f5717adb -> data: something else, prev_hash: 8ef0fbdd7478a8654251efe1791909cfc9f33f71b1427a3a4a85c3f1f5717adb, hash: 395a23c58b1ee581a929f7ac9dda43f69019217a51f622330653a8047e3c9d88 -> data: one last thing, prev_hash: 395a23c58b1ee581a929f7ac9dda43f69019217a51f622330653a8047e3c9d88, hash: e5242b2562825ca60de226b5828a7e39a25e94eb74d36c359b33a3d0bd5c681c

print(chain2)

# returns data: thesamething, prev_hash: None, hash: 52819e76296aa8b77df0560a342333a5c96d309bfe34dc328ac93d0929dd29d4 -> data: thesamething, prev_hash: 52819e76296aa8b77df0560a342333a5c96d309bfe34dc328ac93d0929dd29d4, hash: cd360483bba2f2912ea561bfe49c3c6edd69bf68ed5a0d843e8b4dbb598f8bdb -> data: thesamething, prev_hash: cd360483bba2f2912ea561bfe49c3c6edd69bf68ed5a0d843e8b4dbb598f8bdb, hash: 46195923216e9224de75da8c58c618f09a8376cad9e3e7a05c8238549b14d212

print(chain3) # returns ""
