from rounding import rounding as rnd
import numpy as np
import torch


def G_b(x, b, f):
    return (b*f(x) - x*f(b)) / (f(x) - f(b))

def G_a(x, a, f):
    return (a*f(x) - x*f(a)) / (f(x) - f(a))

def RE_(x1, x0):
    return abs((x1 - x0)/x1)


def falsi_fpi(a,b, epsilon, float_digits, func):
    falsi_fpi_results=[]
    n=0
    RE = 1
    
    # x = torch.tensor(float(a), requires_grad=True)
    # df_dx = torch.autograd.grad(func(x), x, create_graph=True)[0]
    # df_dx_2 = torch.autograd.grad(df_dx, x)[0]

    # alpha = func(a)*df_dx_2.item()
    # falsi_fpi_results.append(('Alpha = ', f"{alpha:.{float_digits-1}e}"))]
    
    alpha = -0.026271019267   # DELETE THIS LINE AND UNCOMMENT THE ABOVE LINES

    if alpha < 0:
        p0=a
        while RE >= epsilon:
            n+=1
            p=G_b(p0, b, func)
            RE = RE_(round(rnd(p, float_digits)[-1], 15), round(rnd(p0, float_digits)[-1], 15))
            falsi_fpi_results.append((n, f"{p0:.{float_digits-1}e}", f"{p:.{float_digits-1}e}", f"{RE:.{float_digits-1}e}"))
            p0=p
            # use G_b

    else:
        p0=b
        while RE >= epsilon:
            n+=1
            p=G_a(p0, a, func)
            RE = RE_(round(rnd(p, float_digits)[-1], 15), round(rnd(p0, float_digits)[-1], 15))
            falsi_fpi_results.append((n, f"{p0:.{float_digits-1}e}", f"{p:.{float_digits-1}e}", f"{RE:.{float_digits-1}e}"))
            p0=p
            # use G_a

    falsi_fpi_results.append(('Approximation of the root is', round(rnd(p, 6)[-1], 10)))
    return falsi_fpi_results