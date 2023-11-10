import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm

def driver():
    x_values = np.linspace(0, 5, 100)  # Define a range of x values

    f = lambda x: math.sin(x)
    T = lambda x: x - (1/6)*x**3 + (1/120)*x**5
    Pa = lambda x: x - (1/6)*x**3
    Pb =  lambda x: x 
    Pc = lambda x: x - (1/6)*x**3 
    
    errT = [abs(f(x) - T(x)) for x in x_values]  # Calculate error values for each x
    errPaPc = [abs(f(x) - Pa(x)) for x in x_values]  
    errPb = [abs(f(x) - Pb(x)) for x in x_values]
    
    plt.figure()    
    plt.plot(x_values, errT)  # Plot x_values on x-axis and errT on y-axis
    plt.plot(x_values, errPaPc)
    plt.plot(x_values, errPb)
    plt.legend(['error Maclaurin', 'error a) c)', 'error b)'])  
    plt.show()

driver()
 
