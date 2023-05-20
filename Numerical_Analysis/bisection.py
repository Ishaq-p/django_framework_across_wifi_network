import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# defining the p_(a,b) , the midpoint of a and b
def p_(a,b):
    return (a+b)/2

# defining the sign of f(a)*f(p), in order to specify whihc side to give the p
def sign_(a,p, f):
    if f(a)*f(p) > 0:
        return True,'+'
    elif f(a)*f(p)<0:
        return False, '-'

# defining the RE, Relative Error
def RE_(p1, p0):
    return abs((p1 - p0)/p1)

def result_list(a, p, b, sign, RE):
    p = round(rnd(p, float_digits)[-1], 10)
    a = round(rnd(a, float_digits)[-1], 10)
    b = round(rnd(b, float_digits)[-1], 10)
    # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    return (a, p, b, sign, RE)

# custom printing function
# def printing(a, p, b, sign, RE):
#     a = rnd(round(a, 10), 7)[-1]
#     b = rnd(round(b, 10), 7)[-1]
#     p = rnd(round(p, 10), 7)[-1]
#     # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
#     print(a,"\t||\t", p,"\t||\t", b,"\t||\t",sign,"\t||\t", RE)



# main function
def bisect(a, b, p0, f, flt, tol=1e-3):
    global float_digits
    float_digits = abs(flt)
    result=[]

    """Find root of f(x) = 0 on interval [a,b] to within tolerance tol."""
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    while RE_(b, a) > tol:
        p1 = p_(a,b)
        sign = sign_(a,p1, f)
        RE = RE_(p1,p0)

        # printing(a, p1, b, sign[1], RE)
        result.append(result_list(a, p1, b, sign[1], RE))

        if sign[0]:
            a = p1
        else:
            b = p1
        p0 = p1
    return result