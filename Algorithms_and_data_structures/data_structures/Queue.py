class Queue:
    def __init__(self,):
        self._begin = self._end = [None, None, None]

    def push(self, value):
        if self._begin[1] is None:
            self._begin[1] = value
            return
        self._begin[0] = [None, value, self._begin]
        self._begin = self._begin[0]
    def pop(self):
        value = self._end[1]
        self._end = self._end[0]
        return value
    def last(self):
        return self._begin[1]
    def first(self):
        return self._end[1]
