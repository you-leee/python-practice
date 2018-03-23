# Given two lowercase strings, S1 and S2, sort S1 in same order as S2.
# If a character in S1 doesn't exist in S2, put them at the end.
# If S1 is "program" and S2 is "grapo", then return "grrapom".

def sameOrder(s1, s2):
    s1_chars = list(s1)
    s2_chars = list(s2)

    result = []
    for c in s2_chars:
        if c in s1_chars:
            c_count = s1_chars.count(c)
            result += [c]*c_count
            for i in range(c_count):
                s1_chars.remove(c)

    result += s1_chars

    return ''.join(result)


# Tests
t1_s1 = "program"
t1_s2 = "grapo"
exp1 = "grrapom"
res1 = sameOrder(t1_s1, t1_s2)
assert exp1 == res1, "Problem: %s != %s" % (exp1, res1)

t2_s1 = "aaaaaa"
t2_s2 = "bbb"
exp2 = "aaaaaa"
res2 = sameOrder(t2_s1, t2_s2)
assert exp2 == res2, "Problem: %s != %s" % (exp2, res2)

t3_s1 = "abcdef"
t3_s2 = "abcdeh"
exp3 = "abcdef"
res3 = sameOrder(t3_s1, t3_s2)
assert exp3 == res3, "Problem: %s != %s" % (exp3, res3)

t4_s1 = "abcdefb"
t4_s2 = "fedcba"
exp4 = "fedcbba"
res4 = sameOrder(t4_s1, t4_s2)
assert exp4 == res4, "Problem: %s != %s" % (exp4, res4)