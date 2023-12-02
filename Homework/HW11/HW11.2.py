import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    
    f = lambda x: x*(np.cos(1/x)) if x != 0 else 0
    a = 0
    b = 1
    n = 5
    # exact integral
    I_ex = 2
    
    I_simp = CompSimp(a,b,n,f)
    print('I_simp= ', I_simp)
    err = abs(I_ex-I_simp)   
    print('absolute error = ', err)    


def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])

    nhalf = n/2
    for j in range(1,int(nhalf)+1):
         # even part 
         I_simp = I_simp+2*f(xnode[2*j])
         # odd part
         I_simp = I_simp +4*f(xnode[2*j-1])
    I_simp= I_simp + f(xnode[n])
    
    I_simp = h/3*I_simp
    
    return I_simp     


    
    
driver()    
