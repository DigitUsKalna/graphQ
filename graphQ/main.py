
import numpy as np 
import  matplotlib.pyplot as plt 
from scipy.optimize import curve_fit








def mean(list_provided):
    return sum(list_provided)/len(list_provided)


def graph_fit(funcToUse, xData, yData, save_it = False, save_path = '.\img.png', x_min=False, y_min = False, y_max=False, x_max=False,x_step = 0.01):

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



def auto_fit(xData, yData,x_step=False):

        
    def func1(x,a,b):
        return a*np.exp(b*x)

    def func2(x,a,b):
        return a*(x**b)

    def func3(x,a,b):
        return a*np.sin(b*x)

    def func4(x,a,b):
        return a*np.cos(b*x)

    def func5(x,a,b):
        return a + b*x

    def func6(x,a,b):
        return a + b/x

    def func7(x,a,b,c):
        return a + b*x + c*x*x

    def func8(x,a,b,c,d):
        return a + b*x + c*x*x + d*x*x*x

    def func9(x,a,b,c,d):
        return a+ b*x + c/x + d*x*x

    func_list = [func1,func2,func3,func4,func5,func6,func7,func8,func9]




    try:
        
        x_min = min(xData)
        x_max = max(xData)
        
        y_min = min(yData)
        y_max = max(yData)
        
        if not x_step:    
            x_step = (x_max-x_min)/100
            
        
        dd = {}
    
        for f in func_list:
    
        
            popt, pcov = curve_fit(f,xData,yData,maxfev=10000)
            
            
            dis_rms = 0
            for i in range(len(xData)):
                y4 = yData[i]
                x4 = xData[i]
                y44 = f(x4,*popt)
            dis_rms += (y4-y44)**2
            dd[dis_rms]=f
        
        funcToUse = dd[min(dd)]
            
        popt, pcov = curve_fit(funcToUse,xData,yData,maxfev=10000)
        
        
        

        xFit = np.arange(x_min,x_max,x_step)

        plt.plot(xFit,funcToUse(xFit, *popt))
        plt.plot(xData,yData,'r.')
        plt.title(str(funcToUse).split()[1][-6:])
        plt.show()
    except:
        plt.plot(xData,yData)
        plt.title("normal")
        plt.plot(xData,yData,'r.')
        plt.show()
    
    


    