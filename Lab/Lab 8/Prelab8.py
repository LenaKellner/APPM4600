import numpy as np
import matplotlib.pyplot as plt


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


# Example 1:
def driver ():
    
    #Ex1
    xeval = np.linspace(0, 10, 1000)
    xint = np.linspace(0, 10, 11)
    indices = indices_of_points_in_subintervals(xeval, xint)
    
    print(indices[0])
    #
    #for i, ind in enumerate(indices):
    #    print(f'Points in subinterval {i}: {ind}')
    
    #EX2
    x0 = 2
    f_x0 = 4
    x1 = 5
    f_x1 = 7

    x_values = np.linspace(x0, x1, 100)
    y_values = evaluate_line(x_values, x0, f_x0, x1, f_x1)
    plt.plot(x_values,y_values)

#indices is a list
#ind is a array of all points in the subintervall
# Print the indices of points in each subinterval

 

driver()

