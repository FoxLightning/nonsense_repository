class LinkedList:
    """
    >>> LList = LinkedList()
    >>> LList.push(1)
    >>> LList.push(2)
    >>> LList.push(3)
    >>> print(LList)
    [3, 2, 1]
    >>> LList.pop()
    3
    >>> LList.pop()
    2
    >>> LList.pop()
    1
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
            if a == None:
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()

