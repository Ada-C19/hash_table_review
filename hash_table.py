class HashTable():
    def __init__(self, size = 10) -> None:
        self.arr = [[] for _ in range(size)]
        self.size = size

    def idx(self, key: str) -> int:
        return hash(key) % self.size

    def insert(self, key, val) -> None:
        index = self.idx(key)
        chain = self.arr[index]

        newEntry = (key, val)
        for i, (k, v) in enumerate(chain):
            # We already have this key in the hash table
            # Replace its value.
            if k == key:
                chain[i] = newEntry
                return
            
        chain.append(newEntry)

    def remove(self, key):
        index = self.idx(key)
        chain = self.arr[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain.pop(i)
                return

    def get(self, key):
        index = self.idx(key)
        chain = self.arr[index]

        for (k, v) in chain:
            if k == key:
                return v
