import numpy as np

def AND(x1, x2):
    x = np.array([0, 1])
    w = np.array([0.5, 0.5])
    b = -0.7
    sum_value = np.sum(w*x) + b
    if sum_value <= 0:
        return 0
    else:
        return 1

# AND(0, 0)
# AND(1, 0)
# AND(0, 1)
# AND(1, 1)
