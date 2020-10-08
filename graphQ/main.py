
import numpy as np 
import  matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def mean(list_provided):
    return sum(list_provided)/len(list_provided)


def graph_fit(funcToUse, xData, yData, save_it = False, save_path = '.\img.png ', x_min=False, y_min = False, y_max=False, x_max=False,x_step = 0.01):

    if x_min and x_max and y_min and y_max :
        pass
    else:
        m = min(xData)
        M = max(xData)
        avg = mean(xData)
        diff = m-m
        x_min = m - (diff/avg)
        x_max = M + (diff/avg)
        m = min(yData)
        M = max(yData)
        avg = mean(yData)
        diff = m-m
        y_min = m - (diff/avg)
        y_max = M + (diff/avg)



    popt, pcov = curve_fit(funcToUse,xData,yData)

    xFit = np.arange(x_min,x_max,x_step)

    plt.plot(xFit,funcToUse(xFit, *popt))
    plt.plot(xData,yData,'r*')

    if save_it:
        plt.savefig(save_path)

    
    


    