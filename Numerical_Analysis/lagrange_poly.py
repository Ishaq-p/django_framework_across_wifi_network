from rounding import rounding as rnd

def RE(p1,p0):
    return abs((p1-p0))/abs(p1)


def L_(xx,x):
    n=len(x)
    L=[]

    for i in range(n):
        L.append(1)
        for j in range(n):
            if i!=j:
                L[i] *= (xx-x[j])/(x[i]-x[j])
    return L


def lagrange_poly(x,y,xx, f_x, sig_digits):
    result=[]
    n=len(x)
    L_i=L_(xx,x)
    L=0
    m=1

    # result.append(('(n)', '(x)', '(y)', '(L)', '(Li*yi)'))
    for i in range(n):
        L += L_i[i]*y[i]
        result.append((m, x[i], y[i], f"{L_i[i]:.{sig_digits-1}e}", f"{L_i[i]*y[i]:.{sig_digits-1}e}"))
        m+=1
    RE_ = f"{RE(f_x,L): .{sig_digits-1}e}"
    result.append((f"L({xx}) = {round(rnd(L, sig_digits)[-1], 15)}", f"RE = {RE_}"))
    return result