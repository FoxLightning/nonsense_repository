# binary search on max settings

def binary_search(m, e):
    """
    Бинарный поиск
    Ищет элемент e в массиве m
    На выходе получаем массив из двух элементов,
    1 элемент это левая граница, например:
    елемент 4 массив [1,3,5]
    ответ будет:
    [1,2]
    так как 4 должна находиться между  3 и 5
    """
    def left_border_search(m, e):
        left_border = -1
        right_border = len(m)
        while right_border - left_border > 1:
            middle = (left_border + right_border)//2
            if m[middle] < e:
                left_border = middle
            else:
                right_border = middle
        return left_border
    def right_border_search(m, e):
        left_border = -1
        right_border = len(m)
        while right_border - left_border > 1:
            middle = (left_border + right_border)//2
            if m[middle] <= e:
                left_border = middle
            else:
                right_border = middle
        return right_border
    return [
        None if left_border_search(m,e) == -1 else left_border_search(m, e),
        None if right_border_search(m, e) == len(m) else right_border_search(m, e)
    ]

def test(func):
    m = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9]
    e = 5
    func_ans = func(m, e)
    right_ans = [6,10]
    print("test 1: {}".format("Ok" if func_ans == right_ans else "Fail"))

    m = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9]
    e = 1
    func_ans = func(m, e)
    right_ans = [2, 4]
    print("test 2: {}".format("Ok" if func_ans == right_ans else "Fail"))

    m = [0, 0, 0, 1, 2, 3, 4, 5, 5, 5, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9]
    e = 0
    func_ans = func(m, e)
    print(func_ans)
    right_ans = [None,3]
    print("test 3: {}".format("Ok" if func_ans == right_ans else "Fail"))

test(binary_search)
