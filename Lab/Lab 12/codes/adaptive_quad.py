# get lgwts routine and numpy
#from gauss_legendre import *

import numpy as np

# gauss legendre quadrature nodes and weights via
# Newton iteration


def driver():
    
    f = lambda x: np.sin(1/x)
    a = 0.1
    b = 2
    
    # exact integral
    I_ex = 2
    
    tol = 10**(-3)
    
    n = 5
    
    #I_trap = eval_composite_trap(a,b,n,f)
    #print('I_trap= ', I_trap)
    
    #err = abs(I_ex-I_trap)   
    
    #print('absolute error = ', err)    
    
    #I_simp = eval_composite_simpsons(a,b,n,f)

    #print('I_simp= ', I_simp)
    
    #err = abs(I_ex-I_simp)   
    
    #print('absolute error = ', err) 
    
    #I_hat = eval_gauss_quad(a,b,n,f)
    #print('I_hat= ', I_hat)
    
    'the following gives errors'
    ##err = abs(I_ex-I_hat)   
    
    ##print('absolute error = ', err)    
    
    ##A_quad = adaptive_quad(a,b,f,tol,n,method)
    ##print ('A_quad=', I,np.unique(X),nsplit )


def lgwt(N,a,b):
  N = N-1
  N1 = N+1
  N2 = N+2
  eps = np.finfo(float).eps  
  xu = np.linspace(N1,-1,1)
  
  # Initial guess
  y = np.cos((2*np.arange(0,N1)+1)*np.pi/(2*N+2))+(0.27/N1)*np.sin(np.pi*xu*N/N2)

  # Legendre-Gauss Vandermonde Matrix
  L = np.zeros((N1,N2))
  
  # Compute the zeros of the N+1 Legendre Polynomial
  # using the recursion relation and the Newton-Raphson method
  
  y0 = 2.
  one = np.ones((N1,))
  zero = np.zeros((N1,))

  # Iterate until new points are uniformly within epsilon of old points
  while np.max(np.abs(y-y0)) > eps:
      
    L[:,0] = one
    
    L[:,1] = y
    for k in range(2,N1+1): 
      L[:,k] = ((2*k-1)*y*L[:,k-1]-(k-1)*L[:,k-2])/k
    
    lp = N2*(L[:,N1-1]-y*L[:,N2-1])/(1-y**2)   
    
    y0 = y
    y = y0-L[:,N2-1]/lp
    
  # Linear map from[-1,1] to [a,b]
  x=(a*(1-y)+b*(1+y))/2
  
  # Compute the weights
  w=(b-a)/((1-y**2)*lp**2)*(N2/N1)**2
  return x,w


def eval_composite_trap(a,b,n,f):
    #if n == 0:
    #  raise ValueError("Number of subintervals (n) cannot be zero.")
    
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    
    I_trap = h*f(xnode[0])*1/2
    
    for j in range(1,n):
         I_trap = I_trap+h*f(xnode[j])
    I_trap= I_trap + 1/2*h*f(xnode[n])
    
    return I_trap, xnode, None  

def eval_composite_simpsons(a,b,n,f):
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
    
    return I_simp, xnode, None  

def eval_gauss_quad(a,b,n,f):
  """
  Non-adaptive numerical integrator for \int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate
  
  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  x,w = lgwt(n,a,b)
  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def adaptive_quad(a,b,f,tol,n,method):
  """
  Adaptive numerical integrator for \int_a^b f(x)dx
  
  Input:
  a,b - interval [a,b]
  f - function to integrate
  tol - absolute accuracy goal
  M - number of quadrature nodes per bisected interval
  method - function handle for integrating on subinterval
         - eg) eval_gauss_quad, eval_composite_simpsons etc.
  
  Output: I - the approximate integral
          X - final adapted grid nodes
          nsplit - number of interval splits
  """
  # 1/2^50 ~ 1e-15
  maxit = 50
  left_p = np.zeros((maxit,))
  right_p = np.zeros((maxit,))
  s = np.zeros((maxit,1))
  left_p[0] = a; right_p[0] = b;
  # initial approx and grid
  s[0],x,_ = method(a,b,n,f);
  # save grid
  X = []
  X.append(x)
  j = 1;
  I = 0;
  nsplit = 1;
  while j < maxit:
    # get midpoint to split interval into left and right
    c = 0.5*(left_p[j-1]+right_p[j-1]);
    # compute integral on left and right spilt intervals
    s1,x,_ = method(left_p[j-1],c,n, f); X.append(x)
    s2,x,_ = method(c,right_p[j-1],n, f); X.append(x)
    if np.max(np.abs(s1+s2-s[j-1])) > tol:
      left_p[j] = left_p[j-1]
      right_p[j] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j] = s1
      left_p[j-1] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j-1] = s2
      j = j+1
      nsplit = nsplit+1
    else:
      I = I+s1+s2
      j = j-1
      if j == 0:
        j = maxit
  return I,np.unique(X),nsplit

driver() 