from sympy.polys.subresultants_qq_zz import *
from sympy import symbols, rem, pprint, Matrix
import itertools
from mpmath import *
from sympy import *
from sympy import Max, Symbol, oo, Min , Interval, Union
from sympy import sympify

def VAS(p,M,space1=[],space2=[]):
    print("\nVAS(",p,",",M,")")
##    space1 = []
##    space2 = []
##    space3 = []
##    space4 = []
    M1=M
    x=var('x')

    p1 = Poly(p)
    p1 = simplify(p1)

    cl = p1.all_coeffs()
    d = len(cl) - 1
    space = []
    
    var_sign = len(list(itertools.groupby((x > 0 for x in cl)))) - 1 #count sign changes
    print("var: ",var_sign)
    
    if var_sign == 0 :
        return None

    if(var_sign == 1):
        a1 = M1.subs({x:0})
        b1 = limit(M1, x, oo)
        a1.evalf()
        b1.evalf()
        a = Min(a1,b1)
        print("a: ", a1 , "b1:" ,b1)
        b = Max(a1,b1)
        if b1 == inf:
            b = ((x**d)*p1.subs({ x : 1/x})).expand()
            b = simplify(b)
        print(" IM IN\n")
        space = [a,b]
        print("space here: " , space)
        return space
    
    p_ub1 = ((x**d)*p1.subs({ x : 1/x})).expand()
    p_ub1 = simplify(p_ub1)
    
    #print(p_ub1)
    ub = LMQ(p_ub1)
    print("ub: ", ub)
    #lb = M1.subs(x,1)
    #print("first lb: ", lb)
    lb = 1/ub
    #print("gamw to spitaki ",lb.is_integer)
    print("lb ", lb)
##    while(1):
##        p1 = p1.subs(x,x+1)
##        p1 = simplify(p1)
##        ub = LMQ(p1)
##        if(sympify(lb).is_integer == False and ub!=0):
##            print("in")
##
##            print("ub ", ub)
##            lb = 1/ub
##            print("im me,",lb)
##        else:
##            break

    if (lb > 1):
        p1 = p1.subs({x : x+lb}).expand()
        p1 = simplify(p1)
        M1 = M.subs({x : x+lb})
        M1 = simplify(M1)
        print("p: " ,p, " , ","M: ", M)
    else:
        p1 = p1.subs({x : x+1}).expand()
        p1 = simplify(p1)
        M1 = M.subs({x : x+1})
        M1 = simplify(M1)
        print("p: " ,p, " , ","M: ", M)
        
    p01=((x+1)**d* p1.subs({x: (1/(x+1))})).expand()
    p01 = simplify(p01)
 
    M01 = M1.subs({x : (1/(x+1))}).expand()
    M01 = simplify(M01)
    print("p01: ", p01, " , " ,"M01: ", M01)
    
    m = M.subs(x,1)
    print("M:",M," m: ",m)
    
    p2 = p1.subs({x:x+1}).expand()
    p2 = simplify(p2)
    
    M2 = M1.subs({x:x+1}).expand()
    M2 = simplify(M2)
    
    r = p1.subs(x,m)
    print("p1oo: " ,p2 , "M1oo: ", M2)
    
    if r!=0:
        space1.append(VAS(p01,M01,space1,space2))
        space2.append(VAS(p2,M2,space1,space2))
        print(space1 ,space2)
        res = Union(space1,space2)
        res = list(filter(None , res))
        return res
    else:
        space1 = VAS(p01,M01)
        space2 = VAS(p2,M2)
        space3 = [m,m]
        space4 = Union(space1,space3)
        
        return Union(space4,space2)



def VCA(p,s):
        
    space1 = []
    space2 = []
    space3 = []
    space4 = []
    
    x = var('x')
    a = s[0]
    b = s[1]
    val = Interval(a,b).boundary
    
    p1 = Poly(p)
    p1 = simplify(p1)
    print("\nVCA(",p,",",val,")")
    cl = p1.all_coeffs()

    d = len(cl) - 1
    p2=(x+1)**d * p1.subs(x,1/(x+1))
    p2 = simplify(p2)
    
    cl2 = p2.all_coeffs()
    
    space=[]
    var_sign = len(list(itertools.groupby((x > 0 for x in cl2))))-1  #count sign changes
    print("var: ",var_sign)
    
    if var_sign == 0 :
        return None

    if(var_sign == 1):
        return val

    p01 = 2**d * p.subs(x,x/2)
    p01 = simplify(p01)
    print("p01/2:  " ,p01)
    
    m = (a+b)/2
    print("m:  " ,m)
    
    p3 = 2**d * p1.subs(x,(x+1)/2)
    p3 = simplify(p3)
    print("p1/2 1:  " ,p3)
    res = p1.subs(x,1/2)
    print("p(1/2)=  " ,float(res))

    
    if(res != 0):
        space1 = VCA(p01,[a,m])
        space2 = VCA(p3,[m,b])
        return (Union(space1,space2))
   
    else:
        space1 = VCA(p01,[a,m])
        space2 = VCA(p3,[m,b])
        space3 = [m,m]
        space4 = Union(space1,space2)
        return Union(space4,space3)

    
def Union(lst1, lst2): 
    my_list = lst1,lst2
    
    final = [] 
    for i in my_list:
        if i != None : 
            final.append(i)        
    return final 

def VAG(p,s):
    print("\n")
    space1 = []
    space2 = []
    space3 = []
    space4 = []
    
    x = var('x')
    a = s[0]
    b = s[1]
    val = Interval(a,b).boundary
    print("(a,b): ", val)
    p1 = Poly(p)
    cl = p1.all_coeffs()
    d = len(cl) - 1
    p2=(x+1)**d * p1.subs(x,(a+b*x)/(x+1))
    p2 = simplify(p2)
    cl2 = p2.all_coeffs()
    space=[]
    var_sign = len(list(itertools.groupby((x > 0 for x in cl2))))-1 #count sign changes
    print("var: ",var_sign)
    
    if var_sign == 0 :
        return 

    if(var_sign == 1):
        return val


    m = (a+b)/2
    print("m: ",m)

    res = p.subs(x,m)
    print("p(m): ",float(res))
    
    if(res != 0):
        space1.append(VAG(p,[a,m]))
        space2.append(VAG(p,[m,b]))
        return (Union(space1,space2))
    
    else:
        space1 = VAG(p,[a,m])
        space2 = VAG(p,[m,b])
        space3 = [m,m]
        space4 = Union(space1,space2)
        return Union(space4,space3)


def LMQ(f):
    x = var('x')
    g= f if LC(f)>0 else -f
    f1 = Poly(f) 
    f_reversed = list(reversed(Poly(g).all_coeffs()))

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

    return ub  


x = var('x')
f = 64*x**7 -112*x**5 + 56*x**3 - 7*x
h = 128*x**8 - 256*x**6 + 160*x**4 - 32*x**2 +1 
p = x**3 -7*x+7
s = x**3 -1*x**2 -2*x +1

#M1 = x
#space=[]
#p1 = Poly(p)
#M1 =  Poly(M1)
space = VAS(p,x)
print(space)
w = 64*x**3 - 28*x + 7
#result = VAG(p,[0,4])
#print(result)
