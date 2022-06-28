from sympy import ZZ

def my_igcd4(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        q = ZZ.quo(old_r, r)

        (old_r, r) = (r, old_r - (q * r))
        (old_s, s) = (s, old_s - (q * s))
        (old_t, t) = (t, old_t - (q * t))

    return (old_s, old_t)

print("The (s, t) of (612, 342) = ", my_igcd4(612, 342))