class Node(object):
    def __init__(self, init_data):
        self.data= init_data
        self.next = None
        
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data= new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class OrderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        current= self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data()> item:
                stop = True
            else: 
                previous = current
                current= current.get_next()
        new_node= Node(item)
        if previous == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

    def print_list(self):
            current= self.head
            while current != None:
                print (current.get_data())
                current= current.get_next()

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found




list= OrderedList()
list.add(27)
list.add(12)
list.add(56)
list.print_list()
print(list.search(54))
            
