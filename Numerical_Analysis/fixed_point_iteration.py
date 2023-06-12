import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA
from sig_digits import sig_digits as sd      # sig_digits.py is in the same folder, its pupose is to find the number of significant digits



# defining the RE, Relative Error
def RE_(x1, x0):
    return abs(abs(x1 - x0)/x1)

# custom printing function
def printing(n, x0, x1, RE):
    x0 = round(rnd(x0, 9)[-1], 12)
    x1 = round(rnd(x1, 9)[-1], 12)
    # RE = rnd(RE, 7)[-1]        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", RE)


# main function
def fixed_point(x0, criterion, float_digits, func):
    fpi_list = []
    interations = 0

    # first iteration
    x1 = func(x0)
    RE = RE_(round(rnd(x1, 9)[-1], 12),round(rnd(x0, 9)[-1], 12))
    fpi_list.append((interations, x0, x1, RE))


    # the middle iterations
    while RE > criterion:
        interations += 1
        x0 = x1
        x1 = func(x0)
        RE = RE_(round(rnd(x1, float_digits)[-1], 12), round(rnd(x0, float_digits)[-1], 12))

        fpi_list.append((interations, rnd(x0, float_digits)[-1], rnd(x1, float_digits)[-1], f"{RE:.{float_digits-1}e}"))
        
    y_ = 6*x1
    pi = np.pi
    RE1 = RE_(pi, y_)

    fpi_list.append((f"x={rnd(x1, float_digits)[-1]}", f"steps={interations+1}, y*={rnd(y_, float_digits)[-1]}, RE={RE1}, SD={sd(RE1)[2]}"))
    print(len(fpi_list))
    return fpi_list
