from rounding import rounding as rnd


def RE_(x1, x0):
    return abs((x1 - x0)/x1)

def secant(x0, x1, epsilon, float_digits, f):
    secant_list=[]
    RE = 1
    n = 1
    while RE >= epsilon:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        RE = RE_(round(rnd(x2, float_digits)[-1], 10), round(rnd(x1, float_digits)[-1], 10))
        
        secant_list.append((n, 
                            round(rnd(x0, float_digits)[-1], 10), 
                            round(rnd(x1, float_digits)[-1], 10), 
                            round(rnd(x2, float_digits)[-1], 10), 
                            RE
                        ))
        x0 = x1
        x1 = x2
        n += 1

    secant_list.append(('Approximation of the root is', round(rnd(x2, 7)[-1], 10)))
    return secant_list