from sympy import ZZ


def my_igcd1(a,b,i):
    if (b==0):
        print("Times =",i,"\n")
        return a

    q=ZZ.quo(a,b)
    r=ZZ.rem(a,b)
    q1=int(ZZ.quo(ZZ.abs(b),2))

    if (r<=q1):
        return my_igcd1(b,a-(b*q),i=i+1)
    else:
        if (q>0): q=q+1
        elif (q<0): q=q-1
        return my_igcd1(b,(b*q)-a,i=i+1)


    
def main():
    i=0
    print("mygcd1")
    gcd=my_igcd1(612,342,i)
    print("GCD of 612 and 342 is = ", gcd,"\n")
    i=0
    gcd=my_igcd1(13,-7,i)
    print("GCD of 13 and -7 is = ", gcd)

if __name__== "__main__":
  main()

