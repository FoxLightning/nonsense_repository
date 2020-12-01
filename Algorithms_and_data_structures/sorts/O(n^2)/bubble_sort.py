def bubble_sort(A):
    """
    Сортировка пузырьком
    O(n**2)
    change input array
    :return input array
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k + 1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A

print(bubble_sort([1,2,1,1,2,2,0,6,7,45,3,2,]))