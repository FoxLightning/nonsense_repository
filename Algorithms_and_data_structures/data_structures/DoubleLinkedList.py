class DoubleLinkedList:
    def __init__(self,):
        self._begin = self._end = [None, None, None]

    def push_left(self, value):
        if self._begin[1] is None:
            self._begin[1] = value
            return
        self._begin[0] = [None, value, self._begin]
        self._begin = self._begin[0]

    def push_right(self, value):
        if self._begin[1] is None:
            self._begin[1] = value
            return
        self._end[2] = [self._end, value, None]
        self._end = self._end[2]


    def pop_left(self):
        value = self._begin[1]
        if self._begin[2] == None:
            self._begin = self._end = [None, None, None]
        else:
            self._begin = self._begin[2]
        return value

    def pop_right(self):
        value = self._end[1]
        if self._end[0] == None:
            self._begin = self._end = [None, None, None]
        else:
            self._end = self._end[0]
        return value


    def last(self):
        return self._begin[1]
    def first(self):
        return self._end[1]



a = DoubleLinkedList()

a.push_right(1)
a.push_right(2)
a.push_right(3)

print(a.pop_left())
print(a.pop_left())
print(a.pop_left())
print(a.pop_left())

a.push_left(1)
a.push_left(2)
a.push_left(3)

print(a.pop_right())
print(a.pop_right())
print(a.pop_right())
print(a.pop_right())


