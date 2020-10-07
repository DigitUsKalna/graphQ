from func import *
import numpy as np 
import  matplotlib.pyplot as plt 
from scipy.optimize import curve_fit



x = np.array([1,2,3,4,5])
y = np.array([1,9,50,300,1500])

popt, pcov = curve_fit(func,x,y)

xFit = np.arange(0.0,5,0.01)

plt.plot(xFit,func(xFit, *popt))
plt.savefig('si.png')