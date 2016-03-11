with open('test.csv') as f:
    for line in f:
        line = line.split(',')
        count = 0
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
	print line1
