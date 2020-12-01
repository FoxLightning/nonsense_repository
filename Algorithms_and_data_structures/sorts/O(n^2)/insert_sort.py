def insert_sort(A):
    """
    Сортировка вставками
    O(n**2)
    change input array
    :return input array
    """
    N = len(A)

    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A

print(insert_sort([2,1,5,1,2,6,1,3,7]))