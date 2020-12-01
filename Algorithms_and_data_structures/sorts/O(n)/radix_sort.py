m = [40, 33, 100, 31, 541, 123, 22, 1, 2, 5]

def radix_sort(array):
    """
    сортировка по разряду
    O(n * m) where m is max number of digits in max number
    replace array
    :return input array
    """
    max_digit = max(array)
    for i in range(1, len(str(max_digit))+1):
        digits = [[] for i in range(10)]
        for j in array:
            index = (j % 10 ** i) // 10 ** (i-1)
            digits[index].append(j)
        counter = 0
        for j in digits:
            for k in j:
                array[counter] = k
                counter += 1
    return array

print(radix_sort(m))


