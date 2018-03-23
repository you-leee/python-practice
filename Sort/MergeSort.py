def mergesort(arr):
    '''
    Implements the mergesort algorithm
    Merge Sort is a Divide and Conquer algorithm.
    It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves
    :param arr: the array to be sorted
    :return: sorted array in ascending order
    '''

    def merge(arr1, arr2):
        if len(arr1) == 0:
            return arr2
        elif len(arr2) == 0:
            return arr1
        else:
            if arr1[0] < arr2[0]:
                return arr1 + arr2
            else:
                return arr2 + arr1

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[0:mid])
    right = mergesort(arr[mid:len(arr)])
    return merge(left, right)
