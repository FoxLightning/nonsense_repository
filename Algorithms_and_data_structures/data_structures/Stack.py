class Stack:
    """
    >>> steck = Stack()
    >>> steck.push(1)
    >>> steck.push(2)
    >>> steck.push(3)
    >>> print(steck)
    [3, 2, 1]
    >>> steck.is_empty()
    False
    >>> steck.top()
    3
    >>> steck.pop()
    3
    >>> steck.pop()
    2
    >>> steck.pop()
    1
    >>> steck.is_empty()
    True
    >>> steck.push(1)
    >>> steck.push(1)
    >>> steck.clear()
    >>> steck.is_empty()
    True
    """

    def __init__(self):
        """
        Create new exemplar of Linked List
        """
        self._begin = None

    def __str__(self):
        """
        convert exemplar to str
        :return: array of all values in linkedlist
        """
        m = []
        a = self._begin

        while True:
            m.append(a[0])
            a = a[1]
            if a is None:
                break
        return str(m)

    def push(self, value):
        """
        input value at begin of LList
        :param value: any object
        """
        self._begin = [value, self._begin]

    def pop(self):
        """
        delete first value
        :return: first value
        """
        assert self._begin is not None, "List empty"
        value = self._begin[0]
        self._begin = self._begin[1]
        return value

    def top(self):
        """
        :return: first value
        """
        assert self._begin is not None, "List empty"
        return self._begin[0]

    def is_empty(self):
        """
        :return: True / False
        """
        return self._begin is None

    def clear(self):
        """
        delete all values in stack
        """
        self._begin = None
    def __iter__(self):
        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()
