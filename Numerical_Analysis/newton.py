from rounding import rounding as rnd
from sympy import *



# defining the RE, Relative Error
def RE_(x1, x0):
    return abs((x1 - x0)/x1)
    
# the iteration function, g(x) = x - f(x) / f'(x)
def g(f, f_, m):
    return m - ( f(m) / f_(m) )


# main function
def newtons(p0, epsilon, float_digits, func, func_):
    result_list=[]
    RE = 1
    n = 1
    
    while RE >= epsilon:
        p = g(func, func_, p0)
        print(p, p0)
        RE = RE_(round(rnd(p, 7)[-1], 10), round(rnd(p0, 7)[-1], 10))
        result_list.append((n, round(rnd(p0, float_digits)[-1], 10), round(rnd(p, float_digits)[-1], 10), f"{RE:.{float_digits-1}e}"))
        p0 = p
        n += 1
    
    result_list.append(('Approximation of the fixed point is', rnd(p, 7)[-1]))
    return result_list