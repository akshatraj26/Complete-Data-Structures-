# if base is negative or float
# if exp is negative or float

def powerOfNumber(base, exp):
    #assert exp >= 0 and int(exp) == exp, "The exponent must be positive number"
    if exp == 0:
        return 1
    if exp == 1:
        return base

    # when exp is negative integer
    if exp < 0:
        return base * powerOfNumber(base, exp+1)
    # if exp < 0 and  float(exp):
    #     return base * powerOfNumber(base, exp+1)

    else:
        return base * powerOfNumber(base, exp-1)

print(powerOfNumber(1.1, -2))


