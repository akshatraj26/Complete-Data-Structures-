"""
gcd(48, 18)
# euclidean method
gcd(a,b)

48/18  2, remainder:12
18/12  1, remainder:6
12/6   2, remainder: 0
6 is the gcd
"""

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The number must be integer"
    if b == 0:
        return a

    if a <0 :
        a = -1 * a

    if  b < 0:
        b = -1 * b
    else:
        return gcd(b, a % b)


print(gcd(-48,  18))