from numpy import loadtxt, zeros, ones, array, linspace, logspace
#from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import pickle
import csv
import numpy as np
from scipy.optimize import curve_fit
x1=[]

def func(x, p1,p2):
  return p1*np.cos(p2*x) + p2*np.sin(p1*x)
loc_submission = "test_mod.csv"
#Load the dataset
out =[]
with open('test_2.csv') as f:
     l = 0 
     for line in f:
	#print l      
	if l==0:
           head= line
        l = l+1
        if l>1:
           line = line.split(',')
           count = 0
           count1 = 0
           fill = 0.000001
           length = -1
           line1 = line[28:147]
           for i in line1:
              length = length + 1
              if i == '':
                 line1[length] = fill
                #print fill
                #count = count + 1
              else:
                 fill = line1[length]
           sub =0
           lin =[]
           for i in line1:
              sub = sub + float(i);
              lin.append(sub)
          # print len(lin)        
           #line[26:209] = lin
          
          # out.append(lin)
          # print len(lin)
           x1=[]
           #x1 = list(range(119))
           for i in xrange(119):
               x1.append(i+2)
           x1 = np.array(x1)
           #print x1   
           #print len(x1)
	   y = lin
           y = np.array(y) 
           #popt, pcov = curve_fit(func, x1, y,p0=(1.0,0.2),maxfev=1000)
           try:
              popt, pcov = curve_fit(func, x1, y,p0=(1.0,0.2),maxfev=5000)
           except RuntimeError:
              print("Error - curve_fit failed")
           p1 = popt[0]
	   p2 = popt[1]
           v = 121
	   lin_new=[] 
           for i in xrange(60):
               x =v+i    
               lin_new.append(p1*np.cos(p2*x) + p2*np.sin(p1*x))
	   
	 #  print len(lin_new)
	   #print lin_new
	   lin_new.append(0)
	   lin_new.append(0) 
	   out.append(lin_new)    
#Plot the data

          # x1 = list(range(179))
         #  y = lin   
          # scatter(x1, y, marker='o', c='b')
           #title('Stock returns')
           #xlabel('Daywise')
           #ylabel('Return value')
     	 #  show()
#with open(loc_submission, "w") as outfile:
#head = head.split(',')
#head = head[26:147]
   #  outfile.writelines(head)
    # outfile.write("\n")
    # pickle.dump(out,outfile)   
     ##  print>>outfile,i   

with open(loc_submission, "w") as outfile:
    outfile.write("Id,Predicted\n")	
    l=1
    k=1
    for i in range(120000):
       k=1
       for j in range(62):
	  s = str(i+1) + '_'+str(j+1)
          outfile.write("%s,%s\n"%(s, out[i][j]))
