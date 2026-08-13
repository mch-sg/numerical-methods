from numerical_methods.utils import *

def RK4solver(dxdt, tspan, x0, n):
    """ 
    Runge-Kutta implementation of order 4
    Where dxdt is the differential equation, like t+x(t).
    Input : x'(t) , [a,b] , x(0) = x0 , n
    Output : timesteps , x values approximating
    """
    a, b = tspan
    t = np.linspace(a, b, n+1)
    h = (b-a)/n
    # Only calc these one time
    hh2 = h / 2
    hh6 = h / 6
    # Init x array and have the first element as x0
    x = np.zeros(n+1)
    x[0] = x0
    
    for i in range(n):
        K1 = dxdt(t[i], x[i])
        K2 = dxdt(t[i] + hh2, x[i] + hh2*K1)
        K3 = dxdt(t[i] + hh2, x[i] + hh2*K2)
        K4 = dxdt(t[i] + h, x[i] + h*K3)
        x[i+1] = x[i] + hh6 * (K1 + 2*K2 + 2*K3 + K4)
    return t, x