import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.arange(1.920, 2.080, 0.001)

# Evaluate p(x) using coefficients
p1_values = x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

# Evaluate p(x) using the expression (x-2)**9
p2_values = (x - 2)**9

# Plot the polynomial
plt.plot(x, p1_values, color='red', label='expanded')
plt.plot(x, p2_values, color='blue', label='nonexpanded')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('expanded vs. nonexpanded form of p(x) = (x-2)^9')
plt.grid(True)
plt.legend()
plt.show()
