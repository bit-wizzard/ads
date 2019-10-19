class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def front(self):
        return self.items[len(self.items) - 1]

q = Queue()

while True:
    a = input().split()

    if(a[0] == 'exit'):
        print('bye')
        break
    elif(a[0] == 'push'):
        q.enqueue(int(a[1]))
        print('ok')
    elif(a[0] == 'pop'):
        print(q.dequeue())
    elif(a[0] == 'front'):
        print(q.front())
    elif(a[0] == 'clear'):
        q.clear()
        print('ok')
    elif(a[0] == 'size'):
        print(q.size())
    else:
        break        