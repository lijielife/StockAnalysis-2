


import pandas as pd
from sklearn.preprocessing import Imputer
import numpy as np
from sklearn import ensemble
from sklearn.ensemble import ExtraTreesRegressor
import re
import random
output=[] 
if __name__ == "__main__":
   loc_train = "./train.csv"
   
   df_train = pd.read_csv(loc_train)
   
   #test = df_test['ID']
   #for i in test:
    #  print i
   #l1  = len(test) 
   #print "var"    
   for i in range(62):
      output.append([])
   first = ['Id']
   allcol = ['Ret_121','Ret_122','Ret_123','Ret_124','Ret_125','Ret_126','Ret_127','Ret_128','Ret_129','Ret_130',
'Ret_131','Ret_132','Ret_133','Ret_134','Ret_135','Ret_136','Ret_137','Ret_138','Ret_139','Ret_140','Ret_141',
'Ret_142','Ret_143','Ret_144','Ret_145','Ret_146','Ret_147','Ret_148','Ret_149','Ret_150','Ret_151','Ret_152',
'Ret_153','Ret_154','Ret_155','Ret_156','Ret_157','Ret_158','Ret_159','Ret_160','Ret_161','Ret_162','Ret_163',
'Ret_164','Ret_165','Ret_166','Ret_167','Ret_168','Ret_169','Ret_170','Ret_171','Ret_172','Ret_173','Ret_174',
'Ret_175','Ret_176','Ret_177','Ret_178','Ret_179','Ret_180','Ret_PlusOne','Ret_PlusTwo']
    
   total = []
   l=0
   train = df_train	
   #t = replicate(6,apply(train[148:209],FUN=median,MARGIN=2))
   tr =[]
   out = []
   sub = 0
   tr_li =[]
   for i in allcol:
      t = train[i]
      tr.append(t)
      temp =[]
       
      for j in t:
         if j =='':
            temp.append(0)   
         else:
            temp.append(j)
      #sub = sub/40000
      sub =0
      tr_li.append(temp) 
      temp.sort()
      #med = random.sample(xrange(40000), 50)
     
      val_list = temp[20000]
      #final=[]
      #val_sum = sum(val)/40000 
      out.append(val_list)
      #print len(val)


print out[60]
print out[61]
with open('median', "w") as outfile:
    outfile.write("Id,Predicted\n")
    l=1
    k=1
    for i in range(120000):
       k=1
       for j in range(62):
          s = str(i+1) + '_'+str(j+1)
          if j>=60:
             
          	outfile.write("%s,%s\n"%(s, out[j]))
          else:
          	outfile.write("%s,%s\n"%(s, out[j]))

    
