import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x_values = np.arange(1.920, 2.080, 0.001)

# Evaluate p(x) using the expression (x-2)^9
p_values = (x_values - 2)^9

# Plot the polynomial
plt.plot(x_values, p_values)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Plot of p(x) = (x-2)^9')
plt.grid(True)
plt.show()