from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import math
from decimal import *

loc_submission = "regressor_submission1.csv"
#Load the dataset
with open('regressor_submission_old.csv') as f:
    output = []
    count =0 
    l = 0
    list1 = []
    for line in f:
        count = count + 1
        if l != 0:
          line = line.split(',')
          if l<63:
             list1.append(line[1])
          else  :
            
	     x = list(range(62))
	     t1 = list1[60].strip()
	     t1 = float(t1) * 0.001
             #print t1  
             t2 = list1[61].strip()
	     t2 = float(t2) * 0.001
	     del list1[-1]
	     del list1[-2]
             #list2 = sorted(list1)
	     #com = 0
	     #for i in list1:
	      #   if i < 0.0009:
		     #com = com +1
	#	     i = i * 0.001
	#	 if i > 0.0001:
	#	     i = float(i) * 0.001
	     #print list2
	     #print com
	     #for i in list2:
                 #i =i.strip()
		 #i = float(i)
                 #print math.modf(i)
	     #ex = list2[com-2]
	     #ex1 = list2[com+2]
	     #print ex
	     #print ex1
            # if ex < -1:
	     #    ex = float(ex.strip())+1
	     #if ex1 > 1:
	#	 ex1 = float(ex1.strip())-1		         	
             #print list1
             #t = list1[30]
             for i in range(60):
                 if list1[i] < 0.0009:
                     #com = com +1
                     list1[i] = list1[i] * 0.001
                 if list1[i] > 0.0001:
                     list1[i] = float(list1[i]) * 0.001
             list1.append(t1)
             list1.append(t2)   				
             y = list1
             output.append(list1)
             #print len(x),len(y) 
#Plot the data
	    # scatter(x, y, marker='o', c='b')
	     #title('Stock returns')
	     #xlabel('Daywise')
	     #ylabel('Return value')
	     #show()
             l=1
             list1 =[] 
             list1.append(line[1])
          if count == 3720001:
             t1 = float(list1[60])*0.001
	     t1 = str(t1)
             t2 = float(list1[61])*0.001
	     t2 = str(t2)
             list1 = sorted(list1)
              #print list1
             t = list1[30]
             for i in range(60):
            	list1[i] = 0
             list1[60]=t1.strip()
             list1[61]=t2.strip()   				
             y = list1
             output.append(list1)     
        l = l +1  

print len(output), 'aa'
print len(output[1])
with open(loc_submission, "w") as outfile:
    outfile.write("Id,Predicted\n")
    l=1
    k=1
    for i in range(60000):
       k=1
       for j in range(62):
          s = str(i+1) + '_'+str(j+1)
	  num = Decimal(output[i][j])
          outfile.write("%s,%.16f\n"%(s,num))
          #output[j][i]
