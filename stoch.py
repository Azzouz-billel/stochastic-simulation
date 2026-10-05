import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# linear congruential generator
def lcg(seed, a, c, m, n):
    """Generate n pseudo-random numbers using a linear congruential generator."""
    random_numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)  # normalize to [0, 1)
    return np.array(random_numbers)
print("Linear Congruential Generator (LCG) Test:")
# Parameters for the LCG
seed = 100
a = 65539
c = 0
m = 2**31
n = 1000# Number of random numbers to generate
# Generate random numbers
random_numbers = lcg(seed, a, c, m, n)
# Display the generated random numbers
print("Generated random numbers:", random_numbers)
#ploting 30 points with black color and alpha 0.5
plt.scatter(range(len(random_numbers[:900])), random_numbers[:900], color='blue', alpha=0.5)
plt.title('Scatter Plot of Generated Random Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
