import numpy as np
import matplotlib.pyplot as plt

def interpolate(x, y):
    # n = len(x)
    V = np.vander(x, increasing=True)
    c = np.linalg.solve(V, y)
    return c

def eval_pol(x, c):
    n = len(c)
    return sum(c[i] * x**i for i in range(n))

def f(x):
    return 1 / (1 + (10 * x)**2)

N = 7  # #of points for the approximation

x_data = np.array([-1 + (i-1) * (2/(N-1)) for i in range(1, N+1)])
y_data = f(x_data)
coefs = interpolate(x_data, y_data)

# Evaluate the polynomial on a finer grid
x_fine = np.linspace(-1, 1, 1001)
y_polynomial = sum(c * x_fine**i for i, c in enumerate(coefs))

# Plot 
plt.plot(x_fine, y_polynomial, label='Interpolating Polynomial')
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot(x_fine, f(x_fine), label='f(x) fine')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("Coefficients:", coefs)
print("Polinomial", y_polynomial)
# # Evaluate the polynomial at x = 5
# result = eval_pol(5, coefs)
# print("Result:", result)