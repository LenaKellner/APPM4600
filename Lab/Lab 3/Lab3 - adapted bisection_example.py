# import libraries
import numpy as np

def driver():

# use routines    
    # f = lambda x: x**3+x-4
    # a = 1
    # b = 4
    f = lambda x: ((x-1)**2) * (x-3)
    a = 0.0
    b = 2.0

    # for endpoints (0.5,2), we get the root x=1 which is correct
    # for endpoints (-1,0.5), we get an error message indicating there is not a root in the interval based on checking if the function has the same sign at the endpoints even though the x=0 root is contained in the interval.
    # For (-1,2), we once again find the root x=1, but not the root at x=0
    # B and C do not find the root at x=0 because that root has multiplicity 2, so the sign is the same at the endpoints and IVT does not apply

    # for 2a, we find the correct root at x=1 approximated as x = 1.0000030517578122 which has 5 digits of accuracy as expected.
    # For 2b, we get an error message which we would expect because the root at x=1 has multiplicity 2 and the condition for IVT will not apply
#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-5

    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))




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
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               

