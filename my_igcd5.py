from sympy import ZZ

def my_igcd5(a, b):

    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        q = ZZ.quo(old_r, r)

        old_r, r = r, old_r - (q * r)
        old_s, s = s, old_s - (q * s)
        old_t, t = t, old_t - (q * t)

    gcd = old_r

    if gcd == 1:
        return old_s
    else:
        return None