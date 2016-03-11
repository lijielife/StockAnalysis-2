from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))


#import plotly.plotly as py
#import plotly.graph_objs as go




#xdata = np.array([-2,-1.64,-1.33,-0.7,0,0.45,1.2,1.64,2.32,2.9])
#ydata = np.array([0.699369,0.700462,0.695354,1.03905,1.97389,2.41143,1.91091,0.919576,-0.730975,-1.42001])

#def func(x, p1,p2):
#  return p1*np.cos(p2*x) + p2*np.sin(p1*x)



#Load the dataset
with open('sample_train.csv') as f:
    for line in f:
        line = line.split(',')
        count = 0

        count1 = 0
        fill = 0.000001
        length = -1
        line1 = line[28:207]
        for i in line1:
            length = length + 1
            if i == '':
                line1[length] = fill
                #print fill
                #count = count + 1
            else:
                fill = line1[length]

        sub1=[]
        sub=0
        count =0
        for i in line1:
        	sub = sub+float(i)
        	sub1.append(sub)
        	count = count + 1
        	

	
	#Plot the data
        plt.figure()
	plt.title('Stock returns')
	plt.xlabel('Daywise')
	plt.ylabel('Return value')
	x = list(range(179))
	y = sub1
        plt.plot(x, y, linewidth=2.0)
        plt.scatter(x, y, s=10, zorder=2)
	#plt.plot(x, y, 'r', lw=3)
	#plt.scatter(x, y, marker='o',c='blue',alpha=0.5)
	#trace1 = go.Scatter(
        #mode = 'lines+markers',
        #name = 'lines+markers'
        #)
        #data = [trace1]
	# Plot and embed in ipython notebook!
	#py.iplot(data, filename='scatter-mode')
	plt.show()
	#sns.distplot(x, hist=False, rug=True);

        #popt, pcov = curve_fit(func, x, y,p0=(1.0,0.2))
        
        
