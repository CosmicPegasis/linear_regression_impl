import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True, threshold=sys.maxsize)

x = np.random.rand(500, 7)
y = np.sum(x, axis=1)
print(repr(x))
print(repr(y))