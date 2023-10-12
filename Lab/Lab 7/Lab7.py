import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():

    f = lambda x: 1/(1+(10*x)**2)
    N = 10

    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    # xint = np.linspace(a,b,N+1)                    #exercise a
    
    # exercise a: 
    # The methods seem to perform very similar, but the more we get to the limits of the intervall, the bigger error gets
    # At N=20, the error is somewhere between 10² and 10³ at point -0.975 and +0.975. 
    # So, as we are getting closer and closer to the limits of the intervall, the error rises
    
    xint = np.zeros(N+1)                            #exercise b
    for j in range (N+1):
        xint[j] = np.cos(((2*(j+1)-1)*np.pi)/(2*N))
    
    # exercise b: 
    # Something with my xint seems to be wrong. 
    # Because for many Ns it is working, but not for N=40 it is not.
    #But if I look at the error, now it differs between the different methods - which it did not before 
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    #xint =/ xeval because xint is the smaller number of points we have whereas xeval is the number that we want
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
    yeval_v = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    
    
    ### create vandermonde: call it so that the program knows about it
    ### call things that you have called before (f.e. ff instead of f_v)
    ### if i do not call something, the program will do nothing (f. e. if i do not m_vander, it will not do something with vandermonde())
    m_vander = vandermonde(f,xint,N)
    ff = f_vector(f,xint,N)
    coefs = a_vector(ff, m_vander)    
    #if a plot shows that something is not right:
    #1) go through it line for line
    #2) print it step by step (f.e. print vandermonde, print a_v, ...) => maybe smth is visibly wrong
    
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
       yeval_v[kk] = eval_polynomial(xeval[kk],coefs, N)
          

    ''' create vector with exact values'''
    fex = f(xeval)
       

    plt.figure()    
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval_l,'bs--') 
    plt.plot(xeval,yeval_dd,'c.--')
    plt.plot(xeval,yeval_v, 'o--')
    plt.legend()

    plt.figure() 
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    err_v = abs(yeval_v-fex)
    plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    plt.semilogy(xeval,err_v,'o--',label='Vandermonde')
    plt.legend()
    plt.show()
    

########################################

def vandermonde(f,x,N):
    i = N+1
    j = N+1
    V = np.zeros((i,j))
    for m in range(N+1):
        for n in range (N+1):
           V[m][n] = x[m]**(n)   #not j-1 because python does count from 0 to (N+1)-1

    return(V)

def f_vector(f, x, N):
    i = N+1
    f_v = np.zeros(N+1)
    for m in range(N+1):
        f_v[m] = f(x[m])
        
    return(f_v)
            
def a_vector(f_v, V):
    a_v =  np.linalg.inv(V) @ f_v
    return(a_v)

def eval_polynomial (x, a_v, N):
    i = N+1
    eval_p = 0
    for m in range (N+1):
        eval_p = eval_p + a_v[m] * x**m
    return(eval_p)
     

#####################################


def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  

''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval
      

driver()        
