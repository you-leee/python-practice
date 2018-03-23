def binary_search(arr, elem):
    '''
    Implements the binary search recursively
    Searches a sorted array by repeatedly dividing the search interval in half depending whether
    the searched element is lower or higher, than the middle element of interval.
    :param arr: sorted array
    :param elem: the element we are searching for
    :return: the index of the element
    '''

    def binary_search_rec(arr, elem, begin_index):
        if len(arr) == 0:
            return -1

        mid = len(arr) // 2

        if arr[mid] == elem:
            return begin_index + mid
        elif elem > arr[mid]:
            return binary_search_rec(arr[(mid+1):len(arr)], elem, mid + 1)
        else:
            return binary_search_rec(arr[0:mid], elem, 0)

    return binary_search_rec(arr, elem, 0)