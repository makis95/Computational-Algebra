from sympy import ZZ

def my_igcd2(a, b, divisions=1):

    if b == 0:
        return a

    q = ZZ.quo(a, b)
    r = ZZ.rem(a, b)

    print("Dividend = ", a, "\tDivisor = ", b, "\tQuotient = ", q, "\tRemainder = ", r, "\tNum divisions = ", divisions)

    if r <= ZZ.quo(ZZ.abs(b) , 2):
        return my_igcd2(b, a - (b * q), divisions + 1)

    elif r > ZZ.quo(ZZ.abs(b), 2):
        if ZZ.quo(a, b) > 0:
            q = q + 1
        else:
            q = q - 1

        return my_igcd2(b, (b * q) - a, divisions + 1)


print("The gcd of (13, -7) is = ", my_igcd2(13, -7))
print("The gcd of (612, 342) is = ", my_igcd2(612, 342))
