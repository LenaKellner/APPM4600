# I've tried to use the pseudocode from textbook p.149f. and test the following example to understand if and how it works. However, it did not work...
# I would have implemented it into the code from before.
# I assume that (Exercise 3.4) the code would have worked even better as all we had before since it's not just using splines as in 3.2 but also using cubix splines. So, the approximations should be even better.

from cmath import e

def natural_cubic_spline(n, x, a):
    # Step 1
    h = [x[i+1] - x[i] for i in range(n-1)]
    
    # Step 2
    alpha = [3/h[i] * (a[i+1] - a[i]) - 3/h[i-1] * (a[i] - a[i-1]) for i in range(1, n-1)]
    
    # Step 3, 4, 5
    l, mu, z = [1], [0], [0]
    for i in range(1, n-1):
        li = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mui = h[i] / li
        zi = (alpha[i-1] - h[i-1] * z[i-1]) / li
        l.append(li)
        mu.append(mui)
        z.append(zi)
    l.append(1)
    z.append(0)
    c = [0] * (n+1)
    c[n] = 0
    
    # Step 6
    for i in range (n-1):    
        for j in range(n-i-1):
            c[j] = z[j] - mu[j] * c[j+1]
            b = (a[j+1] - a[j]) / h[j] - (h[j] * (c[j+1] + 2*c[j])) / 3
            d = (c[j+1] - c[j]) / (3 * h[j])
            print(f"For segment {j}: a={a[j]}, b={b}, c={c[j]}, d={d}")

# Example usage
#n = 3
#x = [0, 1, 2, 3]
#a = [1, e, e**2, e**3]

natural_cubic_spline(n, x, a)  
  
  
  
  
  
  
  
  