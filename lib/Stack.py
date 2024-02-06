class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for item in items:
            if(not self.full()):
                self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if (not self.full()):
            self.items.append(item)
        else:
            return None


    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items)]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit
        
    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1
