a = "колокол"
b = "молоко"

def f_l_d(a,b):
    """
    Нахождение всех возможных вариантов ошибок
    Рекурентным способом
    n = (a + b) / 2
    О(3 ** n) алгоритм совершенно не применим в реальности
    Использовать для чтения, чтобы понять динамический алгоритм
    """
    # базовый случай
    if len(a) == 0 or len(b) == 0:
        return len(a) + len(b)
    # можно взять как за базовый случай, но не обязательно
    elif a[-1] == b[-1]:
        return f_l_d(a[0:-1], b[0:-1])
    # рекурентный случай
    else:
        insert = f_l_d(a, b[0:-1]) + 1
        delete = f_l_d(a[0:-1], b) + 1
        replace = f_l_d(a[0:-1], b[0:-1]) + 1
        return min(insert, delete, replace)

def dynamic_fld(a,b):
    """
    Нахождение кратчайшего расстояния левенштейна
    О(a*b)
    Расстояние левенштейна - сколько нужно сделать исправлений в слове a чтобы получить слово b
    """
    # супер вариант записи массива
    m = [[i+j if i * j == 0 else 0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    # a элемент массива
    # b количество массивов
    for i in range(1, len(b) +1):
        for j in range(1, len(a) +1):
            if a[j-1] == b[i-1]:
                m[i][j] = m[i-1][j-1]
            else: # a[i-1] != b[j-1]
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
    return m[-1][-1]
print(dynamic_fld(a, b))