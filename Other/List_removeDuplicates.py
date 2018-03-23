def rem1(seq):
    elements = {}
    for n in seq:
        elements[n] = 1

    return list(elements.keys())


# Tests
t1 = [1]*1000
exp1 = [1]
res1 = rem1(t1)
assert exp1 == res1, "Problem: %s != %s" % (exp1, res1)

t2 = range(1000)
exp2 = list(range(1000))
res2 = rem1(t2)
assert exp2 == res2, "Problem: %s != %s" % (exp2, res2)

t3 = [1,5,2,3,9,10,10,1,2,4,6,9,1,3,4,11,20]
exp3 = [1,5,2,3,9,10,4,6,11,20]
res3 = rem1(t3)
assert exp3 == res3, "Problem: %s != %s" % (exp3, res3)