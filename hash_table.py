class HashTable():
    SIZE = 10

    def __init__(self) -> None:
        self.arr = [None for _ in range(self.SIZE)]

    def insert(self, key, val):
        index = hash(key) % self.SIZE
        self.arr[index] = val

    def remove(self, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError
