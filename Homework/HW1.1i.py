import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the polynomial
coefficients = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

# Define the range of x values
x_values = np.arange(1.920, 2.080, 0.001)

# Evaluate the polynomial p(x) for each x
p_values = np.polyval(coefficients, x_values - 2)

# Plot the polynomial
plt.plot(x_values, p_values)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Plot of p(x) = (x-2)^9')
plt.grid(True)
plt.show()


