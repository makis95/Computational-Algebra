from sympy import ZZ
from sympy import fraction, Rational, Symbol
from sympy.abc import x, y, z
from sympy import *
from sympy import UnevaluatedExpr

def partial_quo(a,qu_list=[],expr=[],count=0):
    
    a0,a1 = fraction(a)
    q = ZZ.quo(a0,a1)
    a2=ZZ.rem(a0,a1)
    qu_list.append(q)
##    expr = []
##    expr.append(q,a0,a1)
    
    if a1 == 1:
        expression = CFExp(qu_list,q,a0,a1,count)
        return qu_list , expression
        
    if a2 < a1:
        return partial_quo(a1/a2,qu_list,expr,count=count+1)

def CFExp(expr,q,a0,a1,count,i=0):
    f = UnevaluatedExpr(1/(q+UnevaluatedExpr(a1/a0)))
    for el in reversed(expr):
        if i == 0 or i==1:
            i=i+1
            continue 
        f = UnevaluatedExpr(el) + UnevaluatedExpr(1/f)
        i=i+1
    return f    
    


x = Symbol("x")
y = Symbol("y")
expr = x/y
expr=expr.subs([(x, 21), (y, 13)])
quo_list  = []
quo_list ,expr = partial_quo(expr)
print("The partial quontinents list : ",quo_list)
print("Continued fraction expansion : ",expr )
