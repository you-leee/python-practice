def quicksort(arr):
    '''
    Implements the quicksort algorithm
    QuickSort is a Divide and Conquer algorithm.
    It picks an element as pivot and partitions the given array around the picked pivot

    :param arr: the array to be sorted
    :return: sorted array in ascending order
    '''

    def divide(arr, pivot):
        p = arr[pivot]
        left = []
        right = []

        for i in range(len(arr)):
            if i != pivot:
                if arr[i] < p:
                    left.append(arr[i])
                else:
                    right.append(arr[i])

        return left, right

    if len(arr) < 2:
        return arr

    pivot = len(arr) // 2
    left, right = divide(arr, pivot)
    return quicksort(left) + [arr[pivot]] + quicksort(right)
