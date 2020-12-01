def fast_sort(m):
    """
    быстрая сортировка
    O(n * log2(n))
    create a new sorted array
    return: new sorted array
    """
    if len(m) <= 1:
        return m
    elif len(m) == 2:
        if m[1] < m[0]:
            return [m[1], m[0]]
        else:
            return m
    else:
        m1 = fast_sort(m[0:len(m)//2])
        m2 = fast_sort(m[len(m)//2:])

        sorted_list = []

        while True:
            if len(m1) == 0 and len(m2) == 2:
                break
            elif len(m1) == 0:
                sorted_list += m2
                break
            elif len(m2) == 0:
                sorted_list += m1
                break

            if m1[0] < m2[0]:
                sorted_list.append(m1[0])
                del m1[0]
            else:
                sorted_list.append(m2[0])
                del m2[0]
        return sorted_list