#(a)

import numpy as np

# Create vector t with entries starting at 0 incrementing by pi/30 to pi
t = np.array([x*np.pi/30 for x in range(0,31)])

# Create vector y = cos(t)
y = np.cos(t)

# Define the sum S with the upper limit N=let(t)
S = np.sum([t[i]*y[i] for i in range (0, len(t))])

# Print the result
print(f"The sum is: {S}")


#(b)i)

from matplotlib import pyplot as plt

#Define all variables
theta = np.linspace(0,2*np.pi,500)
R = 1.2
deltar = 0.1
f = 15
p = 0

#Define the parametric curve
x = [R*(1 + deltar*np.sin(f*t+p))*np.cos(t) for t in theta]
y = [R*(1 + deltar*np.sin(f*t+p))*np.sin(t) for t in theta]

plt.plot(x,y,'m')
plt.axis('equal')
plt.show()


#(b)ii)
i = np.array(x*1 for x in range (1,11))
R = i
deltar = 0.05
f = 2 + i
p = random.uniform(0,2,none)
for x in (x,y,'m'):
    if x == 10: break
    print (x)