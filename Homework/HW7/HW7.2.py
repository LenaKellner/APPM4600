import numpy as np
import matplotlib.pyplot as plt
import random

def interpolate(x, y):
    # n = len(x)
    V = np.vander(x, increasing=True)
    c = np.linalg.solve(V, y)
    return c

def eval_pol(x, c):
    n = len(c)
    return sum(c[i] * x**i for i in range(n))

def barycentric_lagrange_interpolation(x, f, x_fine):
    n = len(x)
    m = len(x_fine)
    p = np.zeros(m)
    #j = random.randint(0, m)
    w = np.zeros(m)
    #for i in range(m+1):
    #    phi = np.prod(x_fine-x[i]) 
    for j in range (m+1):
        for i in range (m+1):
            if i != j:
                w[j] = 1 / np.prod(x[j] - x[i])  

   # for j in range (n):
    #    if x[j] != x_fine:
     #       pn += (wj * f[j] / (x_fine - x[j]))
      #      pd += (wj / (x_fine - x[j]))
    
    #p = pn/pd 

    for j in range(n):
        wj = 1 / np.prod(x[j] - np.delete(x,j))  
        p += (wj * f[j] / (x_fine - x[j]))
    return p

def f(x):
    return 1 / (1 + (10 * x)**2)

N = 7  # #of points for the approximation
x_data = np.array([-1 + (i-1) * (2/(N-1)) for i in range(1, N+1)])
y_data = f(x_data)
coefs = interpolate(x_data, y_data)

# Evaluate the polynomial on a finer grid
x_fine = np.linspace(-1, 1, 1001)
y_monomial = sum(c * x_fine**i for i, c in enumerate(coefs))
y_barycentric = barycentric_lagrange_interpolation(x_data, y_data, x_fine)

# Plot 
plt.plot(x_fine, y_monomial, label='Interpolating Polynomial Monomial')
plt.plot(x_fine, y_barycentric, label='Interpolating Polynomial Barycentric')
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot(x_fine, f(x_fine), label='f(x) fine')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("Coefficients:", coefs)
print("Polynomial", y_monomial)
# # Evaluate the polynomial at x = 5
# result = eval_pol(5, coefs)
# print("Result:", result)