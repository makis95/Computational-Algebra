from sympy.polys.subresultants_qq_zz import *
from sympy import symbols, rem, pprint, Matrix
import itertools
from mpmath import *
from sympy import *
from sympy import Max, Symbol, oo, Min , Interval, Union

def VAS(p,M,x):
    x=var('x')
    p1 = Poly(p)
   # M1 =  Poly(M)
   # M1 = expand(M1)
    cl = p1.all_coeffs()
    d = len(cl) - 1
    space = []
    var_sign = len(list(itertools.groupby((x > 0 for x in cl)))) - 1 #count sign changes
    print("var: ",var_sign, "\n","p1: " ,p1, "M1: ", M1, "c1: ", cl)
    if var_sign == 0 :
        return 0

    if(var_sign == 1):
        a1 = M.subs(x,0)
        b1 = limit(M, x, oo)
        a1.evalf()
        b1.evalf()
        a = Min(a1,b1)
        print("a: ", a1 , "b1:" ,b1)
        b = Max(a1,b1)
        print(" IM IN\n")
        space = [a,b]
        print("space here: " , space)
 
        return space

    lb = M1.subs(x,1)
    print("first lb: ", lb)
    lb = floor(lb)
    print("lb: ", lb,"\n")
    
    if (lb >= 1):
        p = p.subs(x,x+lb)
        p = simplify(p)
        M = M.subs(x,x+lb)
        M = expand(M)
        print("M: ", M,"\n", "new p: " ,p, "\n")
        
    p01=(x+1)**d * p.subs(x,1/(x+1))
    p01 = simplify(p01)
    print("p01: ", p01, "\n")
    
    M01 = M.subs(x,1/(x+1))
    M01 = simplify(M01)
    print("M01: ", M01, "\n")
    
    m = M1.subs(x,1)
    print("m: ",m,"\n")
    
    p2 = p.subs(x,x+1)
    p2 = simplify(p2)
    
    M2 = M.subs(x,x+1)
    M2 = simplify(M2)
    
    r = p.subs(x,1)
    
    space1 = []
    space2 = []
    space4 = []

    print("p2: " ,p2 ,"M2: ", M2, "r: " ,r,"\n")
    
    if r!=0:
        space1 = VAS(p01,M01,x)
        space2 = VAS(p2,M2,x)
        print("space2:" ,space2)
        res = Union(space1,space2)
        print("res " , res)
        return space1
    else:
        space1 = VAS(p01,M01,x)
        space2 = VAS(p2,M2,x)
        space3 = [m,m]
        space4 = space1.union(space2)
        
        return space4.union(space3)



def VCA(p,s):
        
    space1 = []
    space2 = []
    space3 = []
    space4 = []
    
    x = var('x')
    a = s[0]
    b = s[1]
    p1 = Poly(p)
    cl = p1.all_coeffs()
    print("p1: ", p1, "s: " ,a,b)
    d = len(cl) - 1
    #print("d:", d)
    p2=(x+1)**d * p1.subs(x,1/(x+1))
    p2 = simplify(p2)
    print("p2:  " ,p2,"\n")
    
    cl2 = p2.all_coeffs()
    #print("cl2:  " ,cl2,"\n")
    
    space=[]
    var_sign = len(list(itertools.groupby((x > 0 for x in cl2))))-1  #count sign changes
    print("var: ",var_sign, "\n")
    
    if var_sign == 0 :
        print("ok")
        return None

    if(var_sign == 1):
        space = [a,b]
        return space

    p01 = 2**d * p.subs(x,x/2)
    p01 = simplify(p01)
    print("p01/2:  " ,p01,"\n")
    
    m = (a+b)/2
    print("m:  " ,m,"\n")
    
    p3 = 2**d * p1.subs(x,(x+1)/2)
    p3 = simplify(p3)
    print("p1/2 1:  " ,p3,"\n")
    res = p1.subs(x,1/2)
    print("res:  " ,res,"\n")

    
    if(res != 0):
        space1 = VCA(p01,[a,m])
        space2 = VCA(p3,[m,b])
        print("space1 hi : ", space1 ,"\n", "space2 hey : ", space2)
        
        return (Union(space1,space2))
   
    else:
        space1 = VCA(p01,[a,m])
        space2 = VCA(p3,[m,b])
        space3 = [m,m]
        space4 = Union(space1,space2)
        return Union(space4,space3)

    
def Union(lst1, lst2): 
    final_list = lst1,lst2
    return final_list 

##def VAG(p,(a,b)):
##    p1 = Poly(p)
##    cl = p1.all_coeffs()
##    d = len(cl) - 1
##    p2=(x+1)**d * p1.subs(x,(a+b*x)/(x+1))
##    cl2 = p2.all_coeffs()
##    space=[]
##    var = len(list(itertools.groupby((x > 0 for x in cl2)))) - 1 #count sign changes
##
##    if var == 0 :
##        return 0
##
##    if(var == 1):
##        space.append(a,b)
##        return space
##

##    m = p.subs(x,(a+b)/2)
##    space1 = []
##    space2 = []
##    space3 = []
##    space4 = []
##    res = p.subs(x,m)
##    if(res != 0):
##        space1 = VAG(p,(a,m))
####        space2 = VCA(p,(m,b))
####        return space1.union(space2)
##    else:
####        space1 = VCA(p,(a,m))
####        space2 = VCA(p,(m,b))
####        space3 = [m,m]
####        space4 = space1.union(space2)
####        return space4.union(space3)


x = var('x')
f = 64*x**7 -112*x**5 + 56*x**3 - 7*x
p = x**3 -7*x+7
M1 = x
space=[]
p1 = Poly(p)
#M1 =  Poly(M)
#space= VAS(p1,M1,x)
print(space)
w = 64*x**3 - 28*x + 7
result = VCA(w,[0,4])
print(result)
