from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd


# def f(x):
#     return np.sqrt(1.21*(np.sin(x))**2  +  14.44*(np.cos(x))**2)

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def trapezoidal(a,b,n, flt_digits, f):
    result=[]
    h = (b-a)/n
    sum0 = 0
    sum1 = 0

    for i in range(n+1):
        x = a+i*h
        if i == 0 or i == n:
            sum0 += f(x)
            result.append((i,': \t', round(rnd(x, flt_digits)[-1],10),'\t', round(rnd(f(x)/2, flt_digits)[-1],10)))
        else:
            sum1 += f(x)
            result.append((i,': \t', round(rnd(x, flt_digits)[-1],10),'\t', round(rnd(f(x), flt_digits)[-1],10)))


    sum = round(rnd(h*((sum0/2)+sum1), flt_digits)[-1],10)
    original = round(rnd(integrate.quad(f,a,b)[0], flt_digits)[-1], 7)
    RE_ = RE(original, sum)
    SD = sd(RE_)[-1]

    result.append(("sum0: ", round(rnd(sum0, flt_digits)[-1],7)))
    result.append(("sum1: ", round(rnd(sum1, flt_digits)[-1],7)))
    result.append(("numerical sum: ", sum))
    result.append(("original sum: ", original))
    result.append(("RE: ", RE_))
    result.append(("SD: ", SD))
    return result

# trapezoidal(0,np.pi/2,10, 8)
