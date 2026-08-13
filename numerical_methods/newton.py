from numerical_methods.utils import *

def Newton(f, df, x0, nmax=5):
    x = x0
    X = [x0]
    for _ in range(nmax):
        fx = f(x)
        fp = df(x)
        x = x - fx/fp
        X.append(x)
    return X