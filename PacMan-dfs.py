pr, pc = map(int, input().split())
fr, fc = map(int, input().split())
r, c = map(int, input().split())

grid = []

for i in range(r):
    grid.append(input())
    
class stack:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.iems) - 1]
    
    def size(self):
        return len(self.items)
    
