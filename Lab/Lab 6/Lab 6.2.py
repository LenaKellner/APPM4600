# As you can see, I cannot find the right way to code 3.3. I've tried it in billions of different ways...
# I assume: the less the value of h the less the amount of iterations. Since h is the error of our number, we are nearer if h is small.

# Since I could not figure out the approximate Jacobian, I cannot code 3.4 as well. 
# I assume that Hybrid Newton will need more steps than Slacker Newton - since it does not calculate the precise Jacobians. 
# But, It does calculate several Jacobians, so it should need less steps than Lazy Newton - since it calculates several approximated Jacobians and thereby adapts again and again.

import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1,0])
    
    Nmax = 100
    tol = 1e-10
    
    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)

h = 0.01
# h= 0.001

def f1(x):
    return 4*x[0]**2+x[1]**2-4

def f2(x):
    return x[0]+x[1]-np.sin(x[0]-x[1])

def f1xh(x):
    return 4*(x[0]+h)**2+x[1]**2-4
def f1yh(x):
    return 4*x[0]**2+(x[1]+h)**2-4
def f2xh(x):
    return (x[0]+h)+x[1]-np.sin(x[0]+h-x[1])
def f2yh(x):
    return x[0]+x[1]+h-np.sin(x[0]-x[1]+h)

def evalF(x): 

    F = np.zeros(2)
    
    F[0] = f1(x)
    F[1] = f2(x)
    return F
    
def evalJ(x): 

    J = np.array([[forward_difference_f1xh(f1xh(x), x, h), forward_difference_f1yh(f1yh(x), x, h)] 
        [forward_difference_f2xh(f2xh(x), x, h), forward_difference_f2yh(f2yh(x), x, h)]])
    return J

def forward_difference_f1xh(f, x, h):
    return (f1xh(x) - f1(x)) / h

def forward_difference_f1yh(f, x, h):
    return (f1(x) - f1yh(x)) / h

def forward_difference_f2xh(f, x, h):
    return (f2xh(x) - f2(x)) / h

def forward_difference_f2yh(f, x, h):
    return (f2(x) - f2yh(x)) / h






def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       # h = 10**-7 * np.linalg.norm(x0)
       J = evalJ(x0)
       #J = np.array([[(f1(x0[0] + h, x0[1]) - f1(x0[0], x0[1])) / (h), (f1(x0[0], x0[1] + h) - f1(x0[0], x0[1])) / (h)], 
       # [(f2(x[0] + h, x[1]) - f1(x[0], x[1])) / (h), (f2(x[0], x[1] + h) - f1(x[0], x[1])) / (h)]])
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
        
if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()       
