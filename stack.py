class Stack:  
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(len(self.items), item)
    
    def pop(self):
        return self.items.pop()
    def back(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        return self.__init__()

q = Stack()

while True:
    a = input().split()

    if(a[0] == 'push'):
        q.push(int(a[1]))
        print('ok')
    elif(a[0] == 'pop'):
        print(q.pop())
    elif(a[0] == 'back'):
        print(q.back())
    elif(a[0] == 'clear'):
        q.clear()
        print('ok')
    elif(a[0] == 'size'):
        print(q.size())
    elif(a[0] == 'exit'):
        print('bye')
        break
    elif(a[0]):
        continue