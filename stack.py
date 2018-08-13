class Stack(object):
    def __init__(self):
        self.items= []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peep(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s= Stack()
s.push("ash")
print (s.peep())
print (s.size())
print (s.is_empty())
s.pop()
print (s.is_empty())
