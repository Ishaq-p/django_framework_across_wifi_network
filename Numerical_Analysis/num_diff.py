from rounding import rounding as rnd

def num_diff(x1,h,order,sig_digits, f):
    result=[]
    X=[]
    for i in range(-1,5):
        x = x1+i*h
        y = f(x)
        X.append(x)
        result.append((i, round(rnd(x, sig_digits)[-1], 15), round(rnd(y, sig_digits)[-1], 15)))
    if order==1:
        y1 = (-11*f(X[1]) + 18*f(X[2]) - 9*f(X[3]) + 2*f(X[4]))/(6*h)
        y1 = round(rnd(y1, sig_digits)[-1], 15)
        y1_= f"{y1:.{sig_digits-1}e}"
        result.append((([f"F'(x): {y1_}"])))
    elif order==2:
        y2 = (f(X[0]) - 2*f(X[1]) + f(X[2]))/(h**2)
        y2 = round(rnd(y2, sig_digits)[-1], 15)
        result.append(((f'F"(x): {y2}')))
    else:
        result.append(("sorry we only do untill second order."))
    return result
    