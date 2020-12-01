import stack


def check_wrong_bracket(line):
    """
    >>> check_wrong_bracket("()")
    True
    >>> check_wrong_bracket("([]())()")
    True
    >>> check_wrong_bracket("([)]")
    False
    >>> check_wrong_bracket("()[][")
    False
    """

    open_bracket = "({["
    close_bracket = ")}]"

    for bracket in line:
        if bracket in open_bracket:
            stack.push(bracket)
        elif bracket in close_bracket:
            if stack.top() == open_bracket[close_bracket.rfind(bracket)]:
                stack.pop()
            else:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
