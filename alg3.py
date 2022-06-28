from sympy import ZZ
from sympy import symbols
from sympy import *

def list(M):
    mylist = []

    for el in M:
            r = Symbol(str(el[0]))
            d1 = Symbol(str(el[1]))
            d = Symbol(str(el[2]))
            q = Integer(str(el[3]))
            expr = d1 - d * q
            mylist.append([r, expr])
    print(mylist)

    while (1):
    
        for el in mylist:
            if (el[0] in mylist[-1][1].free_symbols):
                mylist[-1][1]=mylist[-1][1].subs(el[0],el[1])
                print(mylist[-1][0],mylist[-1][1])


        if (mylist[0][0]==0):break
        
                
                
                
                
      
def my_igcd3(a,b,i,M=[]):
    if b==0:
        print("List: ")
        for k in M:
            print(k)
        list(M)
        return a
    
    q = ZZ.quo(a, b)
    r = ZZ.rem(a, b)

    if r!=0 : 
        M.append((r,a,b,q))
    

    if (a>=b):
        return my_igcd3(b,a-(b*q),i=i+1)

    else :
        return my_igcd3(b,(b*q)-a,i=i+1)




def main():
    print("mygcd1")
    i=0
    gcd=my_igcd3(770,567,i)
    print("GCD  = ", gcd)
    
if __name__== "__main__":
  main()
