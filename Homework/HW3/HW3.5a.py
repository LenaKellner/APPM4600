import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x - 4*np.sin(2*x) - 3

# Generate x values
x_values = np.linspace(-10, 10, 500)  

# Calculate corresponding y values
y_values = f(x_values)

# Find zero crossings (where f(x) = 0)
zero_crossings = x_values[np.where(np.diff(np.sign(y_values)))[0]]

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x - 4sin(2x) - 3')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')
plt.scatter(zero_crossings, [0]*len(zero_crossings), color='red', label='Zero Crossings')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Print the number of zero crossings
print(f'There are {len(zero_crossings)} zero crossings.')