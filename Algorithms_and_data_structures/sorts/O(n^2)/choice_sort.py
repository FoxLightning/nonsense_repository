def choice_sort(A):
    """
    сортировка выбором
    O(n**2)
    change input array
    :return input array
    """
    N = len(A)
    for pos in range(N-1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


print(choice_sort([2,1,5,1,2,6,1,3,7]))