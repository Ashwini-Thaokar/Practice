class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash_function(self, old_hash, size):
        return (old_hash+1) % size

    def put(self, key, data):
        hash_value= self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value]= key
            self.data[hash_value]= data
        else:
            if self.slots[hash_value]==key:
                self.data[hash_value]= data   #replace
            next_slot= self.rehash_function(hash_value, len(self.slots))
            while next_slot != None and self.slots[next_slot]!= key:
                next_slot = self.rehash_function(next_slot, len(self.slots))
            if next_slot == None:
                self.slots[next_slot] = key
                seld.data[next_slot] = data
            else:
                self.data[next_slot]= data  #replace

    def get(self, key):
        start_slot= self.hash_function(key, len(self.slots))
        data= None
        stop = False
        found = False
        position= start_slot
        while self.slots[position]!= None and not found and not stop:
            if self.slots[position]== key:
                found = True
                data= self.data[position]
            else:
                position= self.rehash_function(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    

h= HashTable()
h.put(54, "cat")
h.put(26, "dog")
h.put(93, "lion")
print(h.slots)
print(h.data)
print(h.get(54))
