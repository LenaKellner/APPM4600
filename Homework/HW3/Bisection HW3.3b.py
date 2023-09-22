# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: x**3+x-4
    a = 1
    b = 4

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-3

    [astar,ier, iteration] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('itertions =', iteration)



# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       iteration = 0
       return [astar, ier, iteration]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier = 0
      iteration = 0
      return [astar, ier, iteration]

    if (fb ==0):
      astar = b
      ier = 0
      iteration = 0
      return [astar, ier, iteration]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        iteration = 0
        return [astar, ier, iteration]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
      iteration = count
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier, iteration]
      
driver()               

