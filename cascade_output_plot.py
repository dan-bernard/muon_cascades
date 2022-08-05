#reads output file from cascade and writes new file with population values and cascade plot
#must run with python3.4

import numpy as np
import matplotlib.pyplot as plt
import os

Z = []

def findline(phrase, files):
	with open(files) as f:
		for i, line in enumerate(f,1):
			if phrase in line:
				return i

#loops over every file in cascade_outputs
for File in os.listdir('cascade_outputs/'):
	out_file = 'cascade_outputs/' + File
	#print(File)
	name = ""
	filename = name.join(list(File))[:-4]
	print('processing file ' + File)
	text = open(out_file,'r')
	content = text.readlines()
	text.close()
				
					
	#gets maximum n value
	nmx = findline('NMX', out_file)-1
	maxnvalue = int(content[nmx].split()[6])
	#print('max n = ' + str(maxnvalue))
	#print(content[nmx].split())
									
	start = findline(' ' + str(maxnvalue) + ', 0', out_file)
	end = findline(' 1, 0', out_file)

	skip = findline('------------------------------------------------------------------------------------------------------------------------', out_file)

	a = content[skip-1].split()

	pvalues = []

	#reads first three columns (n values, l values and pop values)
	for i in range(start-1, end):
		line = content[i].split()
		
		if line[0] == a[0]:
			pass
			
		else:
			values = [line[i] for i in range(3)]	
			if len(values[0]) == 3 or len(values[0]) == 2:
				n=values[0]
				m = n.split(',')
				values[0] = m[0]
					
			else:
				pop = values[1]
				n=values[0]
				m = n.split(',')
				values[0] = m[0]
				values[1] = m[1]
				values[2] = pop

			floatvalues = [float(x) for x in values]
			pvalues.append(floatvalues[2])

	plist = []
	v = 0

	#adds all pop values in a list of lists
	for j in range(1,(maxnvalue+1)):
		row = []
		for i in range(v, v+(maxnvalue+1)-j):
			row.append(pvalues[i])
		v += (maxnvalue+1)-j
		plist.append(row)
		
	#normalizes data
	for i in range(len(plist)):
		norm = sum(plist[i])
		for j in range(len(plist[i])):
			plist[i][j] /= norm

	#gets Z value
	zline = findline('INPUT CARD NO.  4', out_file) -1
	zvalue = content[zline].split()[-1]
	#print('Z = ' + zvalue)
	Z.append(zvalue)
	
	#gets element
	var = findline('Myonic-', out_file) -1
	a = content[var].split()[7]
	b = list(a)
	element = b[-3] + b[-2]
	#print('element = ' + element)

	# creates new file with population values
	# newfile = open('output_files/' + filename + '.txt', 'w+')
	# newfile.write(element + ' Z = ' + zvalue)
	# newfile.write('\n')

	# n = maxnvalue
	# for i in plist:
	# 	l = 0
	# 	newfile.write('n = ')
	# 	newfile.write(str(n) + ':')
	# 	newfile.write('\n')
	# 	for j in i:
	# 		newfile.write('l = ')
	# 		newfile.write(str(l))
	# 		newfile.write(' population = ')
	# 		newfile.write('{:e}'.format(j))
	# 		newfile.write('\n')
	# 		l += 1
			
	# 	n -= 1

	# newfile.close()

	l = maxnvalue*[i for i in range(maxnvalue)]
	n = []
	for i in range(1,maxnvalue+1):
		for j in range(maxnvalue):
			n.append(maxnvalue+1-i)

	# print(l)
	# print(n)

	weights = []

	for arr in plist:
		count = 0
		while count < maxnvalue:
			if count >= len(arr):
				weights.append(0)

			else:
				weights.append(arr[count])

			count += 1

	# print(weights)

	plt.clf()
	plt.hist2d(l,n, bins = maxnvalue, weights = weights)
	plt.title('Muonic ' + filename + ' cascade')
	plt.xlabel('l')
	plt.ylabel('n')
	plt.colorbar()
	plt.savefig('plots/cascades/' + filename + '_cascade_plot.png')
	plt.show()