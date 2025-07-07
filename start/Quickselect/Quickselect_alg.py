from random import choice

def Quickselect_f(massiv, k):
    L = []
    E = []
    B = []

    pivot = choice(massiv)
    for el in massiv:
        if el < pivot:
            L.append(el)
        elif el == pivot:
            E.append(el)
        else:
            B.append(el)

    if len(L) + len(E) < k:
        return Quickselect_f(B, k - len(E) - len(L))
    elif len(L) + len(E) == k:
        return pivot
    else:
        return Quickselect_f(L, k)
    

massive = [7,2,1,6,8,5,3,4]

res = Quickselect_f(massive, 5)
print(res)
