from numpy import loadtxt, zeros, ones, array, linspace, logspace
#from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import collections
from decimal import *
import operator
import pickle
import csv
import numpy as np
#from scipy.optimize import curve_fit
x1=[]

loc_submission = "output.csv"
#Load the dataset
out =[]
train_list=[]
with open('train.csv') as t:
    l=0
    for line in t:
        if l==0:
            l=l+1
        else:
            #print line
            train_list.append(line)
test_list=[]
with open('test_2.csv') as f:
     l = 0 
     for line in f:
	if l==0:
           head = line
        l = l+1
        if l>1:
           test_list.append(line)

test_1 = 1
for test_acc in xrange(1):
    for line in test_list:
        if test_1>0:
           line = line.split(',')
           count = 0
           count1 = 0
           fill = 0.00000
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
           x1 = list(range(119))
           y = line1
           #print y   
           final_error = 100.0
           error_list=[]
           #with open('train.csv') as t:
           for i in xrange(1):
               skip_var = 0
               
               for train_line in train_list:
                   if skip_var == 0:
                       head = train_line
                   skip_var = skip_var + 1
                   train_stocks=[]
                   #error_list={}
                   if skip_var > 1:
                       train_line = train_line.split(',')
                       fill_missing_data = 0.00000
                       train_stock_length = -1
                       full_train_row = train_line
		       train_stocks = train_line[28:147]
                       for train_stockvalue in train_stocks:
                           train_stock_length = train_stock_length + 1
                           if train_stockvalue== '':
                               train_stocks[train_stock_length] = fill_missing_data
                           else:
                               fill_missing_data = train_stocks[train_stock_length]
                       y = np.array(y,np.float)
                       train_stocks = np.array(train_stocks,np.float)              
                       test_train_error = list(y - train_stocks)
                       #b = [] #a new list with the absolute values
		       #for i in range(0, len(test_train_error)): #going through each of the values in a
     		       #    try:
          	       #        b += [abs(float(test_train_error[i]))] #trying to take the absolute value and put it in the new list (I have the float() because it appears that your 2.40 is a string. If you have it as an actual integer or float (such as 2.40 instead of '2.40') you can just use abs(a[i])
     		       #    except:
          	#	       b += [test_train_error[i]] #if taking the absolute value doesn't work it returns the value on its own.
		       #print(b)
		 #      test_train_error = b
                       test_train_error = sum(test_train_error)
                       if test_train_error > 0:
                           test_train_error = 0+test_train_error
                       else:
                           test_train_error = 0-test_train_error
                       skip_var1 = skip_var-1 
                       #error_list.append((skip_var1,test_train_error))
                       #d = collections.defaultdict(list)

		       #for k, v in error_list:
                       #    d[k].append(v)
                       #print d
                       if final_error > test_train_error:
                           final_error = test_train_error
                           #print final_error
                           similar_train_row = full_train_row
                           train_row = skip_var1
                           #print train_row
                           
                
               print train_row
               out.append(similar_train_row[147:209])
               print len(out) 
               #print final_error        
               #print similar_train_row
               #print d
	       #sorted_errors = sorted(d.items(), key=operator.itemgetter(1))
               #print len(sorted_errors)
               #print sorted_errors
               #train_similar_lines=[]
	       #for i in xrange(10):
               #    train_similar_lines.append(sorted_errors[i][0])
               #print train_similar_lines
     
with open(loc_submission, "w") as outfile:
    outfile.write("Id,Predicted\n")
    l=1
    k=1
    for i in range(120000):
       k=1
       for j in range(62):
          s = str(i+1) + '_'+str(j+1)
	  num = Decimal(out[i][j])
          outfile.write("%s,%.16f\n"%(s,num))








            
