#reads output file from cascade and writes new file with population values and cascade plot
#must run with python3.4


#~ import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os

Z = []

def findline(phrase, files):
	with open(files) as f:
		for i, line in enumerate(f,1):
			if phrase in line:
				return i
				
file_location = 'cascade_outputs/full_shell/'

#loops over every file in cascade_outputs
for File in os.listdir(file_location):
	out_file = file_location + File
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
	#~ print('max n = ' + str(maxnvalue))
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
	
	array = []
#	normalizes data	in plist
	#~ for i in range(len(plist)):
		#~ array = plist
		#~ norm = sum(array[i])
		#~ for j in range(len(array[i])):
			#~ array[i][j] /= norm

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
	#~ print('element = ' + element)

	#creates new file with population values
	#newfile = open('test_output_files/' + filename + '.txt', 'w+')
	#newfile.write(element + ' Z = ' + zvalue)
	#newfile.write('\n')

	#n = maxnvalue
	#for i in plist:
		#l = 0
	#	newfile.write('n = ')
	#	newfile.write(str(n) + ':')
	#	newfile.write('\n')
	#	for j in i:
	#		newfile.write('l = ')
	#		newfile.write(str(l))
	#		newfile.write(' population = ')
	#		newfile.write('{:e}'.format(j))
	#		newfile.write('\n')
	#		l += 1
	#		
	#	n -= 1

	#newfile.close()
	
	#~ for i in range(len(plist)):
		#~ print(sum(plist[i]))
		
	#~ print(File)

	l = maxnvalue*[i for i in range(maxnvalue)]
	n = []
	for i in range(1,maxnvalue+1):
		for j in range(maxnvalue):
			n.append(maxnvalue+1-i)
			
	#~ print(l)
	#~ print(n)
	
	weights = []
	
	for arr in plist:
		count = 0
		while count < maxnvalue:
			if count >= len(arr):
				weights.append(0)
				
			else:
				weights.append(arr[count])
				
			count += 1
	#~ print(weights)
	print_weights = [round(x, 2) for x in weights]
	
	nticks = np.arange(1, maxnvalue+1, 2)	
	lticks = np.arange(0, maxnvalue-1, 2)
	
	if File.startswith('stat'):
		title = 'Muon capture ' + element + ' cascade'
		
	else:
		title = 'Muon transfer ' + element + ' cascade'
	
	plt.clf()
	
	count = 0
	for i in range(len(n)):
		if print_weights[count] != 0:
			plt.text(l[i]+0.5, n[i]+0.5, print_weights[count], fontsize = 'xx-small', color="w", ha="center", va="center", fontweight="bold")
		count += 1
	
	plt.hist2d(l,n, bins = maxnvalue, weights = weights)
	plt.title(title + ' full shell')
	plt.xlabel('l')
	plt.ylabel('n')
	#~ plt.xticks(lticks)
	#~ plt.yticks(nticks)
	plt.colorbar()
	plt.savefig('plots/cascades/printed_values/full_shell/' + filename + '_full_shell_cascade_plot.png')
	#~ plt.show()
	
	#~ print(title)

