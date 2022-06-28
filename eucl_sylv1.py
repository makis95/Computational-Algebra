from sympy.polys.subresultants_qq_zz import *
from sympy import symbols, rem, pprint, Matrix

def euclid_sylv1(f,g,x):
    n = degree(f,x)
    print(n)
    m = degree(g,x)
    print(m)
    k = n+m
    s1 = sylvester(f, g, x, 1) ; pprint( s1 )
    my_rem=s1.det()
    s1.row_del(m-1); s1.row_del(n+m-2); print(s1[:, 0:k-2].det())
    det1= s1[:, 0:k-2].det()
    
    s1.col_swap(k-3, k-2); print(s1[:, 0:k-2].det())
    det2 = s1[:, 0:k-2].det()

    return(det1,det2,my_rem)


x = symbols('x')
f = x**3 + 3*x**2 - 7*x + 7;
g = 3*x**2 + 6*x - 7;
(a,b,my_rem)=euclid_sylv1(f,g,x);
print("[",f,",",g,",",a,"*x+",b,",",my_rem,"]")

