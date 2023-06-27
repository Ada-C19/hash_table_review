class HashTable():
    def __init__(self) -> None:
        self.arr = []

    def insert(self, key, val):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError
class HashTable:
    def __init__(self, size = 10) -> None:
        self.arr = [[] for _ in range(size)]
        self.size = size

    def insert(self, key, val):
        index = hash(key) % self.size
        print(index)
        # if self.arr[index] is not None:
        #     raise KeyError("collision!")
        self.arr[index].append((key, val))

    def get(self, key):
        index = hash(key) % self.size
        for k, v in self.arr[index]:
            if k == key:
                return v