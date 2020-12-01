
def check_brackets(line):
    import stack

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


def stack_calculator(array):
    import stack

    operand = "+-*/^"
    for i in array:
        if i in operand:
            b = stack.pop()
            a = stack.pop()
            if operand.find(i) == 0:
                stack.push(a + b)
            elif operand.find(i) == 1:
                stack.push(a - b)
            elif operand.find(i) == 4:
                stack.push(a ** b)
            elif operand.find(i) == 3:
                stack.push(a / b)
            else:
                stack.push(a * b)
        else:
            stack.push(float(i))

    return stack.pop()


def op_priority(operator):
    operators = [["+", "-"], ["*", "/"], ["^"]]
    for priority_degree in range(len(operators)):
        if operator in operators[priority_degree]:
            return priority_degree


def is_op(sym):
    operators = "-+*/^"
    return True if sym in operators else False


def sort_station(array):
    import stack

    reverse_polish = []

    for token in array:
        if token == ")":
            while stack.top() != "(":
                reverse_polish.append(stack.pop())
            stack.pop()
        elif token == "(":
            stack.push("(")
        elif is_op(token):
            if not stack.is_empty() and is_op(stack.top()) and op_priority(token) < op_priority(stack.top()):
                while not stack.is_empty() and is_op(stack.top()) and op_priority(token) <= op_priority(stack.top()):
                    reverse_polish.append(stack.pop())
                stack.push(token)
            else:
                stack.push(token)
        else:
            reverse_polish.append(token)
    while not stack.is_empty():
        reverse_polish.append(stack.pop())

    return reverse_polish


def pursing_sym(string):
    # token images
    digits = "0123456789"
    operators = "+-*^/"
    brackets = "{[()]}"

    sym_array = []
    prev = " "
    for token in string:
        # for operand
        if token in digits and prev not in digits:
            sym_array.append(token)
        elif token in digits and sym_array[-1] in digits and prev in digits:
            sym_array[-1] += token
        # for operators
        elif token in operators:
            sym_array.append(token)
        # for brackets
        elif token in brackets:
            sym_array.append(token)
        prev = token

    return sym_array


# Script

input_string = input()

pursed_array = pursing_sym(input_string)

if not check_brackets(input_string):
    print("brackets error")

poland_array = sort_station(pursed_array)

print(poland_array)

print(stack_calculator(poland_array))
