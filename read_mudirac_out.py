# code reads ouput mudirac file

text = open('home/muX/mudirac/input/beryllium.xr.out', 'r')
content = text.readlines()

text.close()

# print(len(content))

datalist = []

for i in range(2,len(content)):
	line = content[i].split()
	data = []
	data.append(line[0])
	data.append(float(line[1]))
	# data[line[0]] = float(line[1])
	# print(data)
	datalist.append(data)


# print(datalist)

def avg(array):
	return sum(array)/len(array)

#prints average transition energy 2p-1s
E = []
E.append(datalist[0][1])
E.append(datalist[1][1])
average = avg(E)
print('D21 2p-1s ' + '{:e}'.format(average))


#prints average transition energy 2s-2p
E = []
E.append(datalist[2][1])
E.append(datalist[3][1])
average = avg(E)
print('ESP 2s-2p ' + '{:e}'.format(average))