import sys
from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import matplotlib.pyplot as plt
import pickle
import csv
import operator
import collections
import numpy as np
from scipy.optimize import curve_fit
x1=[]
#Load the dataset
final_buckets_for_each_column = []
for il in xrange(209):
	out =[]
	lin =[]
	real_train=[]
	count=0
	if il >=26:
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
					num = il
                                        print len(line1) 
					lin.append(float(line1[num]))
					real_train.append(float(line1[num]))
		lin.sort()
		out = lin
                #print len(lin)
                print len(out)
		bucket_separation=[]
		for i in xrange(40000):
			if i%200==0 and i>0:
				bucket_separation.append(out[i])
	 	bucket_separation.append(out[39999])
	 	bucket_list_for_real_train=[]
	 	for i in real_train:
	 		for j in xrange(200):
				if bucket_separation[j] >= i:
					bucket_list_for_real_train.append(j) 
					break
		final_buckets_for_each_column.append(bucket_list_for_real_train)
	  	print len(final_buckets_for_each_column)

