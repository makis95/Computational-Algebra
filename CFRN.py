from sympy import floor, pi ,sqrt
from sympy import UnevaluatedExpr

def CFR(a,l,i=0):
    
    a1=a.evalf()
    c1 = floor(a1)
    c1.evalf()
    l.append(c1)
    b2 = a1-c1
    b2.evalf()
    a2 = 1/b2
    a2.evalf()
    
    if (i==13):
        return l
    else :
        CFR(a2,l,i=i+1)

def CFRexpr(expr,i=0):
    f = UnevaluatedExpr(1/(expr[-2]+UnevaluatedExpr(1/expr[-1])))
    for el in reversed(expr):
        if i==0 or i==1 :
            i = i+1
            continue
        f = UnevaluatedExpr(el) + UnevaluatedExpr(1/f)
        i = i + 1

    return f        

a = pi
l = []
CFR(a,l)
print("The fist 13 partial quontinents of ",a," are : \n",l)
expr = CFRexpr(l)
print("Continued fraction expansion is : \n",expr)
print("The fraction in the 13nth iteration is : \n",expr.doit())
print("The decimal form of ",a," is :",expr.doit().evalf())

l = []
a = sqrt(3)
CFR(a,l)
print("The fist 13 partial quontinents of ",a," are : \n",l)
expr = CFRexpr(l)
print("Continued fraction expansion is : \n",expr)
print("The fraction in the 13nth iteration is : \n",expr.doit())
print("The decimal form of ",a," is :",expr.doit().evalf())










    
