class HashTable():
    def __init__(self, size = 10) -> None:
        self.arr = [None for _ in range(size)]
        self.size = size

    def idx(self, key: str) -> int:
        return hash(key) % self.size

    def insert(self, key, val):
        index = self.idx(key)
        print(index, key)
        if self.arr[index] is not None:
            raise KeyError("Hash collision!")
        self.arr[index] = val

    def remove(self, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError
