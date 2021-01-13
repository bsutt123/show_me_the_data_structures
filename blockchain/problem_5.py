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

chain1.append("somthing")
chain1.append("something else")
chain1.append("one last thing")

chain2.append("somthing1")
chain2.append("")
chain2.append("one last thing1")

print(chain1)
print(chain2)
