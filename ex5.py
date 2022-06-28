from sympy import *
from sympy.polys.subresultants_qq_zz import *
from mpmath import *

def sturmSeq(f,x):
    S=[]
    a = Poly(f).coeffs()
    p = f/a[0]
    
    p1 = (f/a[0]).diff()
    S.append(p)
    S.append(p1)
 
    
    while 1 :
        q,r = div(p,p1)
        S.append(r)
        p = (p1*q - r).expand()
        p1 = r
        if S[-1]==0:
            S.remove(0)
            break

    return S
        
    
    
        
def sign_var(num_list):
    s=0
    for i in range(len(num_list)-1):
        if num_list[i]*num_list[i+1]<0:
            s=s+1
    return s                



    
def cauchy_upper_bound(f,x):
    f1 = Poly(f)
    cl = f1.coeffs()
    n = len(cl)
    
    
    #Count and find negative coefficients
    lamda = 0
    for x in cl:
        if x<0:
            lamda = lamda + 1
            c_last = x
            
    #Find Cn-k and k
    pos=cl.index(c_last)
    k=n-pos
    print(c_last,lamda,pos)    
    if(lamda == 0):#No positive roots
        return 0
    
    #Calculation of first interval
    inner=((-lamda*(c_last))/cl[0])
    b=ceil((65/64)*root(inner,k))
    rootIsoInt=[]
    rootIsoInt.append(0)
    rootIsoInt.append(int(b))
    rootIsoInt.append(sign_var(cl))
    return rootIsoInt


def square_free_factors(f,x):
    g=f.diff()
    r = gcd(f,g)
    S=[]
    t,a = div(f,r)
    d = r.diff()
    while(1):
        d = r.diff()
        v=gcd(r,t)
        s,a = div(t,v)
        if d==0:
            S.append(s)
            r = r/v
            t = v
        else : S.append(t)
        if r==1 : break
    return S
        

def rootisolate(Sseq,left,right,eps = 1e-7):



    x = var('x')
    sL = [] 
    sR= []
    interval=[]
    deg = degree(Sseq[0])
    [sL.append(Sseq[i].subs(x,left)) for i in range(deg+1)]
    l_sign=sign_var(sL)
    #rec += 1   #we use this variable to see if it is recursive in order to avoid None returns  
    [sR.append(Sseq[i].subs(x,right)) for i in range(deg+1)]
    r_sign=sign_var(sR)
    roots=l_sign-r_sign

    if right-left<eps: # positive roots

        if roots==0:

            if rec == 1:
                return ["There are no positive roots"]
            else: 
                pass

        if roots==1:
            return [[left,right], 1]   

        if roots > 1:

            res_left = isolate(Sseq,left,(left+right)/2,eps=1e-7)
            res_right = isolate(Sseq,(left+right)/2,right ,eps=1e-7)

            if res_left is not None:
                interval.append(res_left)

            if res_right is not None:
                interval.append(res_right)

            return interval

    else: # negative roots
        if roots==0:

            if rec == 1:
                return ["There are no negative roots"]        
            else:
                pass 

        if roots==1:

            if left != 0:
                return [[-right, -left], 1]        
            else:
                return [[-right, 0], 1]  

        if roots > 1:

            res_left = isolate(Sseq,left,(left+right)/2 , pos_neg = 0, rec = rec)
            res_right = isolate(Sseq,(left+right)/2,right , pos_neg = 0, rec = rec)
            
            if res_left is not None:
                interval.append(res_left)

            if res_right is not None:
                interval.append(res_right)

            return interval
        
        
x = S('x')
f =  x**3 - 7*x + 7
Seq=[]
Seq=sturmSeq(f,x)

square_free_factors(f,x)
interval=[]
interval=cauchy_upper_bound(f,x)
print(Seq)
print(interval)
print(sturm(f))
root=rootisolate(Seq,interval[0],interval[1],1e-7)

f =  32*x**6 - 48*x**4 +18*x**2 - 1
Seq=[]
Seq=sturmSeq(f,x)

square_free_factors(f,x)
interval=[]
interval=cauchy_upper_bound(f,x)
square_free_factors(f,x)
print(Seq)
print(interval)
print(sturm(f))


