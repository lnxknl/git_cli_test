class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        if isinstance(key, str):
            key = sum([ord(c) for c in key])
        return key % self.size

    def set(self, key, value):
        if self.count / self.size > 0.7:  # Load factor threshold
            self._rehash()
        
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))
        self.count += 1
        print(f"Set key {key} at index {hash_index}")

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                self.count -= 1
                return
        raise KeyError('Key not found')

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for item in bucket:
                self.set(item.key, item.value)

# Testing the enhanced HashTable
if __name__ == "__main__":
    ht = HashTable()
    ht.set("apple", 10)
    ht.set("banana", 15)
    ht.set(23, 20)
    ht.set("cat", 25)
    
    print(ht.get("banana"))  # Output: 15
    print(ht.get(23))        # Output: 20
    ht.remove(23)
    try:
        print(ht.get(23))    # Should raise KeyError
    except KeyError as e:
        print(e)

