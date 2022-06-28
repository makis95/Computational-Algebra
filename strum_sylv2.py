from sympy.polys.subresultants_qq_zz import *
from sympy import symbols, rem, pprint, Matrix

def sturm_sylv2(f,g,x):
    n = degree(f,x)
    print(n)
    m = degree(g,x)
    print(m)
    k = n*m
    s2 = sylvester(f, g, x, 2) ; pprint( s2 )
    
    my_rem=s2.det()
    
    s2.row_del(n*m-2); s2.row_del(n*m-2); print(s2[:, 0:k-2].det())
    det1= s2[:, 0:k-2].det()
    
    s2.col_swap(k-3, k-2); print(s2[:, 0:k-2].det())
    det2 = s2[:, 0:k-2].det()

    return(det1,det2,my_rem)




x = symbols('x')
f = x**3 + 3*x**2 - 7*x + 7;
g = 3*x**2 + 6*x - 7;
(a,b,my_rem)=sturm_sylv2(f,g,x);
print("[",f,",",g,",",a,"*x+",b,",",my_rem,"]")
