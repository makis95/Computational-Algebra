from sympy.polys.subresultants_qq_zz import *
from sympy import symbols, rem, pprint, Matrix
from sympy.matrices.expressions import *
from sympy import *
from sympy.polys.numberfields import *

def euclid_amv(f,g,x):

    f1=Poly(f,x)
    f_degree = degree(f)
    a=f1.coeffs()

    g1=Poly(g,x)
    g_degree = degree(g)
    b=g1.coeffs()

    if (f_degree>g_degree):
        c=g1.coeffs()
        j=0
        m = f_degree - g_degree + 2
        n = f_degree + 1
        for i in range(g_degree,f_degree):
            b.append(0)
            c.insert(j,0)
            j=j+1

        M=Matrix([b,c,a])
        M1=euclid_triang(M ,m ,n)
    else :
        c=f1.coeffs()
        j=0
        m = g_degree - f_degree + 2
        n = g_degree + 1
        for i in range(f_degree,g_degree):
            a.append(0)
            c.insert(j,0)
            j=j+1

        M=Matrix([a,c,b])
        M1=euclid_triang(M ,m ,n)

    
    return prs(M,n)


def euclid_triang(M ,m ,n ,i=0 ,j=0):
    pivot = M[i,j]
    c = M[-1,j]
    k=0
    for k in range(n):
        M[-1,k]=c*M[i,k] - pivot*M[-1,k]

    pprint(M)    
    if(i==1 and j ==1):    
        return M   
    else :
        euclid_triang(M,m,n,i+1,j+1)

def prs(M,n):
    x = symbols('x')
    i=n
    rem = 0*x
    for i in range(n-1,0,-1):
        p = M[-1,i]
        rem= rem + p*x**((n-1)-i)

    l=[]
    l.append(rem)
    return l


x = symbols ('x')
f = x**3 + 3*x**2 - 7*x + 7
g = 3*x**2 + 6*x -7
rem = euclid_amv(f,g,x)
print(rem)

f = x**4 - x**3 + x**2 - 7*x + 7
g = 4*x**3 - 3*x**2 + 2*x -7
rem = euclid_amv(f,g,x)
print(rem)

f = 5*x**2 - 82*x + 105
g = 4*x**3 - 3*x**2 + 2*x -7
rem = euclid_amv(f,g,x)
print(rem)


