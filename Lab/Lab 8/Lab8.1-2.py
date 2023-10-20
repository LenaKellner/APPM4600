import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 

#3.2: It performs way better than the methods at lab7. The error is smaller - both at the mid of the interval and at the end; no runge effect

def driver():
    
    #f = lambda x: math.exp(x)
    f = lambda x: 1/(1+(10*x)**2)
    #a = 0
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    #plt.legend()
    plt.show() 
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show() 
        
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    ind = indices_of_points_in_subintervals(xeval, xint)
    
    for jint in range(Nint):

        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        indind = ind[jint]
        
        for kk in range(len(indind)):
             yeval[indind[kk]] = evaluate_line(xeval[indind[kk]], a1, fa1, b1, fb1)
        
    return yeval
          
            
     
           
def indices_of_points_in_subintervals(xeval, xint):
    indices = []

    for i in range(len(xint)-1):
        ind = np.where(np.logical_and((xeval >= xint[i]) , (xeval < xint[i+1])))
        indices.append(ind)
    return indices

def evaluate_line(x, x0, f_x0, x1, f_x1):
    m = (f_x1 - f_x0) / (x1 - x0)
    b = f_x0 - m * x0
    return m * x + b
          
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
