from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import pickle
import csv
import operator
import collections
import numpy as np
from scipy.optimize import curve_fit
x1=[]

#Load the dataset
out =[]
lin ={}
count=0
with open('train.csv') as f:
     l = 0 
     for line in f:
	if l==0:
           head= line
        l = l+1
        if l>1:
           line = line.split(',')
           count = count+1
           count1 = 0
           fill = 0.000001
           length = -1
           line1 = line[26:209]
           for i in line1:
              length = length + 1
              if i == '':
                 line1[length] = fill
                #print fill
                #count = count + 1
              else:
                 fill = line1[length]
           sub =0
           #lin['id']=count
           #lin.append((float(line1[119])-float(line1[120]))-(float(line1[120])-float(line1[121]))) 
           lin[count]=float(line1[27])
newlin=[]
od = sorted(lin.items(), key=operator.itemgetter(1))
#od = collections.OrderedDict(sorted(lin.items())) 
#print od[0][0]
v=0
for k in od:
    print k
    newlin.append(k[0])
    #v=v+1
    #print v
#print newlin
           #for i in line1:
            #  sub = sub + float(i);
             # lin.append(sub)
          # print len(lin)        
           #line[26:209] = lin
          
#neg=0
#lin.sort()
#for i in newlin:
#    if i<0:
#        neg=neg+1
#print neg 
#print newlin[0]
#print newlin[39999]         
print len(newlin)
x1 = list(range(40000))
print len(x1)
y = newlin   
scatter(x1, y, marker='o', c='b')
title('Stock returns')
xlabel('Daywise')
ylabel('Return value')
show()
    
#with open(loc_submission, "w") as outfile:
#head = head.split(',')
#head = head[26:147]
   #  outfile.writelines(head)
    # outfile.write("\n")
    # pickle.dump(out,outfile)   
     ##  print>>outfile,i   

             
