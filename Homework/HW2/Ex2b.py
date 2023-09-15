import numpy as np

# Definieren der Matrix A
A = np.array([[1 - 10**10, 10**10],
              [1 + 10**10, -10**10]])

# Berechnung der Singulärwerte
singular_values = np.linalg.svd(A, compute_uv=False)

# Die euklidische Norm ist der größte Singulärwert
euclidean_norm = max(singular_values)

print("Euklidische Norm von A:", euclidean_norm)

# Definieren der Matrix B
B = np.array([[0.5, 0.5],
              [0.5*(1 + 10**(-10)), 0.5*(1 - 10**(-10))]])

# Berechnung der Singulärwerte
singular_values = np.linalg.svd(B, compute_uv=False)

# Die euklidische Norm ist der größte Singulärwert
euclidean_norm = max(singular_values)

print("Euklidische Norm von B:", euclidean_norm)