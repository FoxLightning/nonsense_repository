# Тест стека
"""
>>> is_empty()
True
>>> push(3)
>>> push(2)
>>> top()
2
>>> push(1)
>>> is_empty()
False
>>> pop()
1
>>> pop()
2
>>> is_empty()
False
>>> clear()
>>> is_empty()
True
"""


def push(value):
    """
    add value on top
    :returns nothing
    """
    _stack.append(value)


def pop():
    """
    remove value from top
    :returns top value
    """
    return _stack.pop()


def is_empty():
    """
    check: stack is empty?
    :returns True or False
    """
    return len(_stack) == 0


def clear():
    """
    clear stack
    :returns nothing
    """
    _stack.clear()


def top():
    """
    show top element on stack
    :returns top element
    """
    return _stack[-1]


def show():
    """
    show all stack
    :return stack list
    """
    return _stack


if __name__ == "__main__":
    """
    run test if file running as a main program
    """
    import doctest
    doctest.testmod()


_stack = []  # initialization stack
