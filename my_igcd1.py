from sympy import ZZ
from sympy import fraction, Rational, Symbol
from sympy.abc import x, y
from sympy import *

def CFExp(q,a0,a1,expansion):
    print(q,a0,a1)
    a= Symbol(str(a0))
    b = Symbol(str(a1))
    q = Integer(str(q))
    expr = q + 1/(b/a)
    expansion.append(expr)
    return expr

    





def partial_quo(a,qu_list=[],expansion=[]):
    
    a0,a1 = fraction(a)
    q = ZZ.quo(a0,a1)
    a2=ZZ.rem(a0,a1)
    qu_list.append(q)

    if a1 == 1:
        print(expansion)
        return qu_list
        
        
    CFExp(q,a0,a1,expansion)
    
    if a2 < a1:
        return partial_quo(a1/a2,qu_list,expansion)




x = Symbol("x")
y = Symbol("y")
expr= x/y
expr=expr.subs([(x, 21), (y, 13)])
quo_list=[]

quo_list=partial_quo(expr)
print(quo_list)

