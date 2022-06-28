from sympy import ZZ, Symbol, Integer

def aux_igcd3(rem_list):
    rem_aux = []

    for eq in rem_list:
        rem = Symbol(str(eq[0]))
        D = Symbol(str(eq[1]))
        d = Symbol(str(eq[2]))
        q = Integer(str(eq[3]))
        expr = D - d * q
        rem_aux.append([rem, expr])

    print("Base expression: ", rem_aux[-1][0], " = ", rem_aux[-1][1])

    while True:
        count = 0

        for symbol in rem_aux:
            if symbol[0] in rem_aux[-1][1].free_symbols:
                count = count + 1
                rem_aux[-1][1] = rem_aux[-1][1].subs(symbol[0],symbol[1])
                print("Expr after substitution: ", rem_aux[-1][0], " = ", rem_aux[-1][1])

        if count == 0:
            break

    return rem_aux[-1][1].args[0].args[0], rem_aux[-1][1].args[1].args[0]


def my_igcd3(a, b, divisions=1, rem_list=[]):

    if b == 0:
        return aux_igcd3(rem_list)
        return a

    q = ZZ.quo(a, b)
    r = ZZ.rem(a, b)

    if r != 0:
        rem_list.append((r, a, b, q))

    print("Special Array: ")
    for i in rem_list:
        print(i)

    if a >= b:
        return my_igcd3(b, a-(b*q), divisions + 1)
    else:
        return my_igcd3(a, (b*q)-a, divisions + 1)



(s, t) = my_igcd3(612, 342)
print("The (s, t) of (612, 342) are = ", (s, t))
