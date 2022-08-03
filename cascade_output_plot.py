#reads output file from cascade and writes new file with population values and cascade plot
#must run with python3.4

import numpy as np
import matplotlib.pyplot as plt
import os

Z = []

transferpop2 = {}
transferpop3 = {}
statpop2 = {}
statpop3 = {}


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
		
	#pop2 = sum(plist[-2])
	#pop3 = sum(plist[-3])
		
	#normalizes data	
	#for i in range(len(plist)):
		#norm = sum(plist[i])
		#for j in range(len(plist[i])):
			#plist[i][j] /= norm

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

	def cumulative(func):
		count = 0
		r = np.random.random()
		while r >0:
			r -= func(count)
			count += 1
		return count
		
	#appends functions to list
	lambdas = []

	for i in range(len(plist)):
		f = (lambda l, n=i:(plist[n][l] if l<len(plist[n]) else 0))
		lambdas.append(f)
		
	x = []
	y = []

	#creates the plot and saves it as png
	for i in range(500000):
		n = int(np.random.random() * len(lambdas))+1
		x.append(cumulative(lambdas[n-1]))
		y.append(maxnvalue-n+1)
	
	plt.clf()	
	plt.hist2d(x,y, bins = maxnvalue, density = True)
	plt.xlabel('l')
	plt.ylabel('n')
	plt.title('Muonic ' + filename + ' cascade dist')
	plt.colorbar()
	plt.savefig('plots/cascades/' + filename +'_cascade_plot.png')
	plt.show()
	
	# if File.startswith('transfer'):
	# 	transferpop2[int(zvalue)] = sum(plist[-2])
	# 	transferpop3[int(zvalue)]= sum(plist[-3])
	
	# if File.startswith('stat'):
	# 	statpop2[int(zvalue)] = sum(plist[-2])
	# 	statpop3[int(zvalue)] = sum(plist[-3])
		

# plt.clf()
# plt.scatter(transferpop2.keys(), transferpop2.values())
# plt.title('transfer 2 population')
# plt.savefig('test_pop_plots/transfer_2_pop')
# plt.show()

# plt.clf()
# plt.scatter(transferpop3.keys(), transferpop3.values())
# plt.title('transfer 3 population')
# plt.savefig('test_pop_plots/transfer_3_pop')
# plt.show()

# plt.clf()
# plt.scatter(statpop2.keys(), statpop2.values())
# plt.title('stat 2 population')
# plt.savefig('test_pop_plots/stat_2_pop')
# plt.show()

# plt.clf()
# plt.scatter(statpop3.keys(), statpop3.values())
# plt.title('stat 3 population')
# plt.savefig('test_pop_plots/stat_3_pop')
# plt.show()

# print(transferpop2.values())
# print(transferpop2.keys())
 
