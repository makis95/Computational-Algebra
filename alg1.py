from sympy import ZZ



def my_igcd1(a,b):
    if b==0: return a

    if (a>=b): return my_igcd1(b,a-b)
    else : return my_igcd1(a,b-a)



def main():
    print("mygcd1")
    gcd=my_igcd1(612,342)
    print("GCD of 618 and 342 is = ", gcd)


if __name__== "__main__":
  main()





                
