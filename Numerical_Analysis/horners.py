import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# custom printing function
def printing(a, alpb, b):
    a = round(a, 10)
    if alpb == 0:       # if the value is 0 and i round it it will return 1, so therefore i have to check if it is 0 and if it is i will return 0
        alpb = 0
    else:
        alpb= round(alpb, 10)
    b = round(b, 10)
    # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(a,"\t||\t", alpb,"\t||\t", b)



# main function
def horners(alpha, coefs):
    result=[]
    b0 = 0
    # print(coef[0],"\t||\t", 0,"\t||\t", b0)

    for a in coefs:
        alpb = rnd(alpha*b0, 7)[-1]
        b = rnd(a + alpb, 7)[-1]
        result.append((a, alpb, b))
        b0 = b
    return result  
        

