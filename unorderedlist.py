import node
class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current != None:
                count += 1
                current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and found is False:
                if current.get_data() == item:
                        found = True
                else:
                        current = current.get_next()
        return found
    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


list = UnorderedList()
list.insert(12)
list.insert(27)
list.insert(3)
print(list.search(27))
