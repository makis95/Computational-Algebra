from sympy import *
from sympy import solve
from sympy.polys.subresultants_qq_zz import *
from mpmath import *



def LMQ(f):
    x = var('x')   
    f1 = Poly(f) 
    f_reversed = list(reversed(Poly(f).all_coeffs()))

    c = f1.all_coeffs()
    n = len(f_reversed)
    d = len(c) - 1

    ub = 0
    if(n <= 1):
        ub = 0
        return ub
    
    t = [1]*n

    for m in range(n-1,0,-1):
        if f_reversed[m-1] < 0 :
            index=0
            temp_ub=S("oo")
            for j in range(n,m,-1) :
                if f_reversed[j-1] > 0:

                    temp=((2.0**t[j-1])*(-f_reversed[m-1]/f_reversed[j-1]))**(1.0/(j-m))
                    t[index] = t[index] + 1
                    if(temp_ub > temp):
                            temp_ub = temp
                            index = j-1
                            
            if(ub < temp_ub):
                ub = temp_ub
    
    return(ceiling(ub))
    







x = var('x')
w = x**3 + 6*x**2 + 5*x + 1
f = x**3 + (10**100)*x**2 - (10**100)*x - 1
p = x**3 -7*x +7
ub = LMQ(p)
print("ub = ",ub)
