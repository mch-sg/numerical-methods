from numerical_methods.utils import *

# Vi tager x-punkter og evaluerer det i'te cardinalpolynomie
def CardinalPolynomial(knuder, i, t):
    cout = []
    li = 1
    # Vi definerer cardinalpolynomiet (som på side 181)
    for j in range(len(knuder)):
        if(j!=i):
            li *= (x - knuder[j]) / (knuder[i] - knuder[j])

    return li

# Find the interpolation of lagrange form (p. 181) of the p_n
def InterpolerLagrangeForm(knuder, ydata, t):
    pn = 0
    cout = []

    # Sum over li(x) * f(x_i)  NOT evaluated at t
    for i in range(len(knuder)):
        li  = CardinalPolynomial(knuder, i, t)
        pn += li * ydata[i]

    # Now evaluate at t
    for val in t:
        cout.append(pn.subs({x:val}))

    return cout