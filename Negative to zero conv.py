import numpy as np

a = np.array([1, 2, -3, 4, -5, -6])
print("Input:", a)

a[a < 0] = 0
print("Result:", a)