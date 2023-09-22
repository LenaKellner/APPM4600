import numpy as np

def aitkens(seq0, tol, Nmax):

    # input
    #   seq0 - input sequence of linear convergence
    #   tol - tolerance
    #   Nmax - maximal number of iterations
    
    # output
    #   xstar - final approximation of the sequence
    #   seqa - the sequence of approximations created by Aitkens method applied to seq0
    #   count - number of iterations in the sequence = the length of seqa
    #   ier - error message
    
    seqa = np.zeros((Nmax+1, 1))
    count = 0
    pn = seq0[count]
    pn1 = seq0[count+1]
    
    while (count < Nmax):
        # set the variables for the equation to calculate the nth term of the Aitkens sequence
        pn = seq0[count]
        pn1 = seq0[count + 1]
        pn2 = seq0[count + 2]
        
        # calculate the nth term of Aitkens sequence
        pn_a = pn- ((pn1 - pn)**2) / (pn2 - 2*pn1 + pn)
        
        #add to the output vector
        seqa[count] = pn_a
        
        # if the n - (n-1) terms have reached the stopping tolerance, set xstar as pn_a
        if (abs(pn_a - seqa[count - 1]) < tol): 
            xstar = pn_a
            ier = 0
            return [xstar, seqa, ier, count]
        count = count + 1
    xstar = pn_a
    ier = 1
    return [xstar, seqa, ier, count]