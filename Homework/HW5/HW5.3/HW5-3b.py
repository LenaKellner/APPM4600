import numpy as np

# Initial guess
x, y, z = 1, 1, 1

# Number of iterations
Nmax = 5

# Empty Array for the errors
errors=[]

for i in range(Nmax):
    # Calculate f, f_x, f_y, f_z
    f = x**2 + 4*y**2 + 4*z**2 - 16
    fx = 2*x
    fy = 8*y
    fz = 8*z
    
    # Calculate the correction using the iteration scheme
    denominator = fx**2 + fy**2 + fz**2
    correction_x = f * fx / denominator
    correction_y = f * fy / denominator
    correction_z = f * fz / denominator
    
    # Update x, y, z
    x -= correction_x
    y -= correction_y
    z -= correction_z
    
    # Compute the error, append it and create the quotient
    error = np.linalg.norm((f))
    errors.append(error)
    quotient = np.array(errors[i]) / np.array(errors[i-1])**2

    # Print results
    print(f"Iteration {i+1}: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}, f(x, y, z) = {f:.6f}")
    print("Quotient :", quotient)