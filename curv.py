
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------data -------------------
def curve_func(x, a, b, c, d, e):
    return a/(b*x**3+c*x**2+d*x+e)

if __name__ == '__main__':
    


    df_hu = pd.read_excel(f'data.xlsx', sheet_name = 'sheet')


    x_data = df_hu[['User_MHZ']]
    y_data = df_hu[['DL_User_Throughput']]


    x_data = np.asanyarray(x_data)
    y_data = np.asanyarray(y_data)

    x_data = x_data.flatten()
    y_data = y_data.flatten()

    y_data = np.nan_to_num(y_data)
    x_data = np.nan_to_num(x_data)

    popt, _ = curve_fit(curve_func, x_data, y_data, maxfev=10000)

    a, b, c, d, e = popt

    x_line = np.arange(min(x_data), max(x_data), 1)
    y_line = curve_func(x_line, a, b, c, d, e)


    final = 'y=%.5f/%.5f*x+%.5f*x^2+%.5f*x^3+%.5f' % (
        a, d, c, b, e)

    print(f'eq_7: {final}')

    print(f'''----------- coeficients
    {round(a, 5)}
    {round(b, 5)}
    {round(c, 5)}
    {round(d, 5)}
    {round(e, 5)}
    ---------------------''')


    plt.plot(x_line, y_line, '--', color='red', linewidth=4)
    plt.legend()
    plt.style.use('bmh')
    plt.show() 
    # ----------------------------------------------------------------------------
