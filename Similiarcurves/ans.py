import pandas as pd
#testf = pd.read_csv('test.csv')
df = pd.read_csv('test_mod.csv')
#for i in df['Predicted']:
x=[]
lin=[]
final=[]
dum=[]
out=[]
six2=0
for i in xrange(7440000):
    six2=six2+1
    dum.append(df['Predicted'][i])
    if six2==62:	
        x.append(dum)
        six2=0
        dum=[]
#print x
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
           zero_count=0
           for j in x[l-2]:
               if j==0:
                   zero_count= zero_count+1
                   if zero_count ==1:
                       final.append(-0.000258448576704)
                   if zero_count ==2:
                       final.append(-0.000257912011802)
               #if zero_count ==2:
               #    break
               final.append(j-sub)
               sub =j
           out.append(final)

with open('subans.csv', "w") as outfile:
    outfile.write("Id,Predicted\n")
    l=1
    k=1
    for i in range(120000):
       k=1
       for j in range(62):
          s = str(i+1) + '_'+str(j+1)
          outfile.write("%s,%s\n"%(s, out[i][j]))

#print len(lin)
#print len(x)

#for i in lin :
#    zero_count=0
#    for j in x :
#        if j==0:
#            zero_count= zero_count+1
#        if zero_count ==2:
#            break
#        final.append(j-i)
   
    
         
        
