def combinations(elems, k):
    if k == 0:
        return []

    if k == len(elems):
        return elems.copy()

    n = len(elems)

    def innerComb(n, k, arr, result):
        for i in range(n, -1, -1):
            if(i >= k):
            # choose the first element
                arr[k-1] = elems[i-1]
                if (k > 1):
                    # if still needs to choose
                    # recursive into smaller problem
                    innerComb(i - 1, k - 1, arr, result)
                else:
                    # print out one solution
                    result.append(arr.copy())

        return result

    arr = [0]*k
    result = []
    innerComb(n, k, arr, result)
    return result



t1 = [1,2,3]
k = 0
exp1 = []
res1 = combinations(t1, k)
assert(exp1 == res1)

t2 = [1,2,3,4]
k = 3
exp2 = [[1,2,3], [1,2,4], [1,3,4], [2,3,4]]
res2 = combinations(t2, k)
print(res2)