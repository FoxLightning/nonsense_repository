def sort_by_selection(a):
    """
    Сортировка выбором
    in worst O(n**2)
    but average O(n * log2(n))
    create a new sorted array
    return: new sorted array
    """
    if len(a) < 2:
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            return [a[1],a[0]]
        else:
            return a
    else:
        less = []
        more = []
        equal = []
        for i in range(1,len(a)):
            if a[i] > a[0]:
                more.append(a[i])
            elif a[i] == a[0]:
                equal.append(a[i])
            elif a[i] < a[0]:
                less.append(a[i])
        ans = sort_by_selection(less) + equal + [a[0]] + sort_by_selection(more)
        return ans