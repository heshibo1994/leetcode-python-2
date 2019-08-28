def PowerWithUnsignedExponent(base, absExponent):
    result = 1.0
    for i in range(absExponent):
        result = result *base
    return result


def fun(base, exponent):
    g_InvalidInput = False
    if base == 0 and exponent < 0:
        g_InvalidInput = True
        print(g_InvalidInput)
        return 0
    if exponent < 0:
        return PowerWithUnsignedExponent(base, -exponent)
    else:
        return PowerWithUnsignedExponent(base, exponent)

print(fun(2,3))
print(fun(2,-3))
print(fun(0,-3))
