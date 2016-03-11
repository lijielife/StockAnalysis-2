import pandas as pd
from sklearn.preprocessing import Imputer
import numpy as np
from sklearn import ensemble
from sklearn.ensemble import ExtraTreesRegressor
 
if __name__ == "__main__":
   loc_train = "./train.csv"
   loc_test = "./test.csv"
   loc_submission = "regressor.submission.csv"
 
   df_train = pd.read_csv(loc_train)
   df_test = pd.read_csv(loc_test)
   output = []
   for i in range(62):
      output.append([])
   first = ['Id']
   allCol = ['Ret_121','Ret_122','Ret_123','Ret_124','Ret_125','Ret_126','Ret_127','Ret_128','Ret_129','Ret_130',
'Ret_131','Ret_132','Ret_133','Ret_134','Ret_135','Ret_136','Ret_137','Ret_138','Ret_139','Ret_140','Ret_141',
'Ret_142','Ret_143','Ret_144','Ret_145','Ret_146','Ret_147','Ret_148','Ret_149','Ret_150','Ret_151','Ret_152',
'Ret_153','Ret_154','Ret_155','Ret_156','Ret_157','Ret_158','Ret_159','Ret_160','Ret_161','Ret_162','Ret_163',
'Ret_164','Ret_165','Ret_166','Ret_167','Ret_168','Ret_169','Ret_170','Ret_171','Ret_172','Ret_173','Ret_174',
'Ret_175','Ret_176','Ret_177','Ret_178','Ret_179','Ret_180','Ret_PlusOne','Ret_PlusTwo']
   allcol = ['Ret_121','Ret_122','Ret_123','Ret_124','Ret_125','Ret_126','Ret_127','Ret_128','Ret_129','Ret_130',
'Ret_131','Ret_132','Ret_133','Ret_134','Ret_135','Ret_136','Ret_137','Ret_138','Ret_139','Ret_140','Ret_141',
'Ret_142','Ret_143','Ret_144','Ret_145','Ret_146','Ret_147','Ret_148','Ret_149','Ret_150','Ret_151','Ret_152',
'Ret_153','Ret_154','Ret_155','Ret_156','Ret_157','Ret_158','Ret_159','Ret_160','Ret_161','Ret_162','Ret_163',
'Ret_164','Ret_165','Ret_166','Ret_167','Ret_168','Ret_169','Ret_170','Ret_171','Ret_172','Ret_173','Ret_174',
'Ret_175','Ret_176','Ret_177','Ret_178','Ret_179','Ret_180','Ret_PlusOne','Ret_PlusTwo']

   last=['Weight_Intraday','Weight_Daily']
   total = []
   l=0	
   	
   for i in allcol:
      print l	
       	
      total = first + allCol + last
      #print total
      
      feature_cols = [col for col in df_train.columns if col not in total]           
      train = df_train[feature_cols]
      feature_cols1 = [col for col in df_test.columns if col not in first] 
      test = df_test[feature_cols1]
      test = Imputer().fit_transform(test)	
      
      i=str(i)
      #print i
      y = df_train[i]	  	
      y = df_train[i].astype('float32')     	
      y = y.fillna(0)     
     # print y
      test_ids = df_test['Id']     
      classification = ExtraTreesRegressor(n_estimators=500,max_depth=None, min_samples_split=2)   
      X = Imputer().fit_transform(train)
      	
     # y = Imputer().fit_transform(y)
     
      print len(X[1])
      print len(test[1])
      print len(y)	
      classification.fit(X, y)
      out = list(classification.predict(test))
      print len(out)
      #print out
      #break
      df_test[i]=out
      output[l]=out
      l =l +1
      #test[i]=[]
      #for e, val in enumerate(out):
           
     # with open(loc_submission, "w") as outfile:
      #  outfile.write("Id,Type\n")
       # for e, val in enumerate(out):
        #  outfile.write("%s,%d\n"%(test_ids[e],val))
      allCol.remove(i)

with open(loc_submission, "w") as outfile:
    outfile.write("Id,Predicted\n")
    l=1
    k=1
    for i in range(60000):
       k=1
       for j in range(62):
          s = str(i+1) + '_'+str(j+1)
          outfile.write("%s,%s\n"%(s,output[j][i]))
          #output[j][i]
          
                
                                                                                                    

