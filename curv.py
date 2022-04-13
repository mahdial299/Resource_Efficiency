
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------data -------------------
x_data = []

y_data = []
# ------------------------------------ function equation --------

def curve_func(x, a, b, c, d, e):
    return a/(b*x**3+c*x**2+d*x+e)

popt, xamarin = curve_fit(curve_func, x_data, y_data)

a, b, c, d, e = popt

x_line = np.arange(min(x_data), max(x_data), 1)
y_line = curve_func(x_line, a, b, c, d, e)

plt.plot(x_line, y_line, '--', color='red', label='Baseline', linewidth=4)
plt.show()

# ----------------------------------------------------------------------------
