m = [5, 1, 7, 1, 2, 9, 10, 23, 2, 2, 2, 1, 11, 15]

def frequency_analysis(array):
    """
    сортировка частотным анализом
    O(n + m) where m is max value in sequence
    replace array
    :return input array
    """
    # create an array with counters number
    frequency = [0] * (max(array)+1)
    for i in m:
        frequency[i] += 1
    counter = 0
    for i in range(len(frequency)):
        for j in range(frequency[i]):
            array[counter] = i
            counter += 1
    return array

def f_a_d(array):
    d = {}
    mv = []
    for i in array:
        # D[name] = D.pop(name, 0) + 1
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            mv.append(i)
    iter = 0
    for key in sorted(mv):
        for j in range(d[key]):
            array[iter] = key
            iter += 1
    return array







print(f_a_d(m))