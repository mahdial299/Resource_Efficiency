
import os
import pyfiglet
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
from sklearn import impute
import xlsxwriter
import matplotlib.pyplot as plt
from posixpath import split
from win10toast import ToastNotifier
from tqdm import tqdm
from datetime import datetime, timedelta


e = datetime.now()

splitter = '-'*60

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

def file_reminder():
    startf = datetime.now() - timedelta(6)
    stopf = datetime.now() + timedelta(1)
    print('you need to have these dates CU : ')
    categ = []
    for item in range(int(startf.day), int(stopf.day)):
        categ.append(item)
    print(*categ)
        

def ban():
    print(C + f'''{pyfiglet.figlet_format("Efficiency")}''' + R + f'''
{splitter}''' + W)

def t_l():
    print(f'''{R + splitter + W}
    1. Raw data scatter
    2. New Raw data baseline and plot
    3. Raw data scatter + baseline
    4. Province excel generator


    0 for main console
{R + splitter + W}''')

def objective(x, a, b, c, d,e):
    return a/(b*x**3+c*x**2+d*x+e)

os.system('cls' if os.name == 'nt' else 'clear')

kameron = ToastNotifier()
while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    ban()

    file_reminder()

    t_l()

    userArg = int(input("Enter task number : "))

    match userArg:
        case 1:
            plt.scatter(x,y, label = 'Raw data',color = 'blue')
            plt.style.use("bmh")
            plt.legend()
            plt.show()
            
        case 2:

            popt, _ = curve_fit(objective, x, y)

            a, b, c, d, e = popt

            x_line = np.arange(min(x), max(x), 1)

            y_line = objective(x_line, a, b, c, d, e)

            plt.plot(x_line, y_line, '--', color='red', label = 'Baseline' ,linewidth =4)

            final = 'y = %.5f / %.5f * x + %.5f * x^2 + %.5f * x^3 + %.5f' % (a,d, c, b, e)

            print(f'''

            x_line sample : 
            {x_line[0:4]}

            y_line sample : 
            {y_line[0:4]}
            ''')

            print(C + f'new equation : ' + G + f'{final}'+ W)
            plt.legend()
            plt.style.use("bmh")
            plt.show()
        
        case 3:

            plt.scatter(x,y, label = 'Raw data',color = 'blue')
            plt.style.use("bmh")

            popt, _ = curve_fit(objective, x, y)

            a, b, c, d, e = popt
            x_line = np.arange(min(x), max(x), 1)

            y_line = objective(x_line, a, b, c, d, e)

            plt.plot(x_line, y_line, '--', color='red', label = 'Baseline' ,linewidth =4)

         
            plt.legend()
            plt.style.use("bmh")
            plt.show()
            
        case 4:

            popt, _ = curve_fit(objective, x, y)
            a, b, c, d, e = popt


            x_line = np.arange(min(x), max(x), 1)
            y_line = objective(x_line, a, b, c, d, e)

            plt.plot(x_line, y_line, '--', color='blue', linewidth =4)

            final = 'y=%.5f/%.5f*x+%.5f*x^2+%.5f*x^3+%.5f' % (a,d, c, b, e)


            n_a = float(final[2:10])
            n_b = float(final[11:18])
            n_c = float(final[21:28])
            n_d = float(final[34:41])
            n_e = float(final[46:54])


            print(n_a)
            print(n_b)
            print(n_c)
            print(n_d)
            print(n_e)

            print(f''' ----- Coefficients --------  
            a = {n_a}
            b = {n_b}
            c = {n_c}
            d = {n_d}
            e = {n_e}''')


            province_list = ['AR','QN','ZN','BU','HZ','LN','KD','KS','HN','FS','ES','AG','AS','IL','KZ','TH','KM','QM']
            for z in range(len(province_list)):
                x2 = []
                y2 = []
                AG_sector = []
                for i in range(len(pro)):
                    if pro[i] == province_list[z]:
                        x2.append(x[i])
                        y2.append(y[i])
                        AG_sector.append(sector[i])
                print(len(AG_sector))
                plt.scatter(x2, y2, color='yellow')

# ------------------------QN WORST CELLS

                x3 = []
                y3 = []
                AG_worst = []
                for i in range(len(pro)):
                    if pro[i] == province_list[z]:
                        if y[i] < n_a / (n_b * x[i] + n_c * (x[i] ** 2) - n_d * (x[i] ** 3) + n_e):
                            AG_worst.append(sector[i])
                            x3.append(x[i])
                            y3.append(y[i])
                print(len(AG_worst))
                plt.scatter(x3, y3, color='red')

# -----------------------------SORT
                diff = []
                for i in range(len(AG_worst)):
                    diff.append((n_a / (n_b * x3[i] + n_c * (x3[i] ** 2) - n_d * (x3[i] ** 3) + n_e)) - y3[i])

#------------------------------excel 
            
                outWorkbook = xlsxwriter.Workbook(str(province_list[z])+"_CELLS.xlsx")
                outSheet = outWorkbook.add_worksheet()
                outSheet.write("A1", "CELLS")
                outSheet.write(0, 0, "SECTORS")
                outSheet.write(0, 1, " Worst SECTORS")
                outSheet.write(0, 2, "User per MHz")
                outSheet.write(0, 3, "User throughput")
                outSheet.write(0, 4, "DISTANCE TO EXPECTED THROUGHPUT")

                for i in range(len(AG_sector)):
                    outSheet.write(i + 1, 0, AG_sector[i])
                for k in range(len(AG_worst)):
                    outSheet.write(k + 1, 1, AG_worst[k])
                for j in range(len(x3)):
                    outSheet.write(j + 1, 2, x3[j])
                for m in range(len(y3)):
                    outSheet.write(m + 1, 3, y3[m])
                for m in range(len(diff)):
                    outSheet.write(m + 1, 4, diff[m])
                outWorkbook.close()    

                # for chico in tqdm(range(z), ncols= 50):
                #     sleep(0.25)
            plt.show()

#-------------------------excel_baseline_file generator
            outWorkbook2 = xlsxwriter.Workbook("2_Baseline_CELLS.xlsx")
            outSheet2 = outWorkbook2.add_worksheet()
            outSheet2.write(0, 0, "x")
            outSheet2.write(0, 1, "y")
            for k in range(len(x_line)):
                outSheet2.write(k, 0, x_line[k])
            for k in range(len(y_line)):
                outSheet2.write(k, 1, y_line[k])
            outWorkbook2.close()
        case 0:
            os.chdir(r'C:\Users\Mehdi Alebrahim\Desktop')
            os.system('python hello.py')



