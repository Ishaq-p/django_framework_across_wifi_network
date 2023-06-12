from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd


# def f(x):
#     return np.exp(2.08*np.sin(x))

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def simpson(a,b,n, flt_digits, f):
    result =[]
    h = (b-a)/n
    sum0 = 0
    sum1 = 0
    sum2 = 0

    for i in range(n+1):
        x = a+i*h
        if i == 0 or i == n:
            sum0 += f(x)
            result.append((i, round(rnd(x, flt_digits)[-1], 10), round(rnd(f(x), flt_digits)[-1], 10), round(rnd(f(x), flt_digits)[-1], 10)))
        elif i%2==0:
            sum2 += f(x)
            result.append((i, round(rnd(x, flt_digits)[-1], 10), round(rnd(2*f(x), flt_digits)[-1], 10),  round(rnd(2*f(x), flt_digits)[-1], 10)))
        else:
            sum1 += f(x)
            result.append((i, round(rnd(x, flt_digits)[-1], 10), round(rnd(4*f(x), flt_digits)[-1], 10),  round(rnd(4*f(x), flt_digits)[-1], 10)))
    
    sum = round(rnd( h/3*(sum0+(4*sum1)+(2*sum2)) , flt_digits)[-1], 8)
    # y = round(integrate.quad(f,a,b)[0], 8)
    y = 4*sum
    RE_ = RE(np.pi, y)
    SD = sd(RE_)[-1]

    # print("sum0: ", round(sum0,8))
    # print("sum1: ", round(sum1,8))
    # print("sum2: ", round(sum2,8))
    result.append(("\nnumerical sum: ", sum))
    # print("original sum: ", y)
    result.append(("y: ", y))
    result.append(("pi: ", round(rnd(np.pi, flt_digits)[-1], 10)))
    result.append(("RE: ", RE_))
    result.append(("SD: ", SD))
    return result

