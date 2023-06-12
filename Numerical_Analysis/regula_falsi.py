from rounding import rounding as rnd


def RE_(x1, x0):
    return abs((x1 - x0)/x1)


def xINT(a, b):
    return a - (f(a) * (a - b) / (f(a) - f(b)))


def regular_falsi(a, b, epsilon, float_digits, func):
    global f
    f = func
    rf_list=[]
    RE=1
    n=1
    p0=a
    p=a

    # while RE >= epsilon:
    while abs(f(p)) > epsilon:

        p = xINT(a, b)
        RE = RE_(round(rnd(p, float_digits)[-1], 10), round(rnd(p0, float_digits)[-1], 10))

        rf_list.append((n, round(rnd(a, float_digits)[-1], 10), 
                        round(rnd(p, float_digits)[-1], 10), 
                        round(rnd(b, float_digits)[-1], 10), 
                        f"{rnd(f(a), float_digits)[-1]:.{float_digits-1}e}", 
                        f"{rnd(f(p), float_digits)[-1]:.{float_digits-1}e}", 
                        f"{rnd(f(a)*f(p), float_digits)[-1]:.{float_digits-1}e}", 
                        f"{RE:.{float_digits-1}e}"))

        Hot_Cold = f(a) * f(p)
        if Hot_Cold < 0:
            b = p
            p0 = p
        else:
            a = p
            p0 = p
        n += 1

    rf_list.append(('Approximation of the root is', round(rnd(p, 6)[-1], 10)))
    return rf_list