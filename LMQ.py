from sympy import *
from sympy import solve
from sympy.polys.subresultants_qq_zz import *
from mpmath import *



def LMQ(f):
    
    f1 = Poly(f)
    c = f1.all_coeffs()
    pairs = []
    x = var('x')
    t = [1]*len(c)
    for i in range(len(c)):
        if c[i] < 0 :
            for j in range(len(c)-1) :
                if c[j] > 0:
                    a = c[j]/2**t[j]*x**(len(c)-j-1)
                    b = c[i]*x**(len(c)-i-1)
                    pairs.append([a,b])
                    t[j] = t[j] + 1
                    s=solve(a+b)
                    print(s)

    print(pairs)
    







x = var('x')
f = x**3 + (10**100)*x**2 - (10**100)*x - 1
LMQ(f)
