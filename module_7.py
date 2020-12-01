class Queue:
    def __init__(self, *v):
        self.a = list(v)
        self.qty = len(self.a)
        self.cur = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.qty > self.cur:
            self.cur += 1
            return self.a[self.cur-1]
        else:
            raise StopIteration
    def push(self, *v):
        self.a += list(v)
        self.qty += len(v)
    def pop(self):
        self.qty -= 1
        return self.a.pop()



a = Queue(1,2,3,4)
a.push(5,6)
print(a.pop())
for i in a:
    print(i)

