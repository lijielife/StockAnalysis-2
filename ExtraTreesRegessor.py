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
   for i in allcol:
      total = first + allCol + last
      print total
      #print df_train.columns
      feature_cols = [col for col in df_train.columns if col not in total] 
      # print feature_cols
      #X_train = np.dtype(np.float64)
      #X-train.dtype="float32"
      X_train = df_train[feature_cols]
      #print X_train
      X_test = df_test[feature_cols]
      i=str(i)
      print i
      #y = np.dtype(np.float64)
      y = df_train[i].astype('float32')
      y = y.fillna(0)
      #print df_train[i]
      #y.fillna(0)
      #y.dtype="float32"
      #np.any(np.isnan(y))
      #print type(y)
      #y=y.view('float32')
      print y
      test_ids = df_test['Id']
      #print test_ids
      del df_train
      del df_test
      classification = ExtraTreesRegressor(n_estimators=10,max_depth=None, min_samples_split=2)   #rf = Pipeline([("scale", StandardScaler()),("rf", RandomForestClassifier(n_estimators=10, 2))])
      X = Imputer().fit_transform(X_train)
      y = Imputer().fit_transform(y)
      classification.fit(X_train, y)
      del X_train
      with open(loc_submission, "w") as outfile:
        outfile.write("Id,Type\n")
        for e, val in enumerate(list(classification.predict(X_test))):
          outfile.write("%s,%d\n"%(test_ids[e],val))
      allCol.remove(i)
                                                                                                  

