import numpy as np

def f(x):
  return np.cos(x)

def forward_difference(f, x, h):
  return (f(x + h) - f(x)) / h

def centered_difference(f, x, h):
  return (f(x + h) - f(x - h)) / (2 * h)

# Set the initial value of h
h = 0.01 * np.power(2, -np.float64(np.arange(0, 10)))

# Compute the forward and centered difference approximations
forward_differences = forward_difference(f, np.pi / 2, h)
centered_differences = centered_difference(f, np.pi / 2, h)

# Print the results
print("Forward difference approximations:", forward_differences)
print("Centered difference approximations:", centered_differences)
print(h)
