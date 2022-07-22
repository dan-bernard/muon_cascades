import matplotlib.pyplot as plt
import os

#only with transfer/stat intensity files at a time

int3s2p = {}
int3s2p['name'] = '3s-2p'
int3d2p = {}
int3d2p['name'] = '3d-2p'
int2s2p = {}
int2s2p['name'] = '2s-2p'
int3p2s = {}
int3p2s['name'] = '3p-2s'
int3d2s = {}
int3d2s['name'] = '3d-2s'
int2p1s = {}
int2p1s['name'] = '2p-1s'
int3p1s = {}
int3p1s['name'] = '3p-1s'
int3d1s = {}
int3d1s['name'] = '3d-1s'

pop2s = {}
pop2s['name'] = '2s'
pop2p = {}
pop2p['name'] = '2p'
pop3d = {}
pop3d['name'] = '3d'
pop3p = {}
pop3p['name'] = '3p'
pop3s = {}
pop3s['name'] = '3s'


def intensity(filename):
	text = open('intensities/stat/' + filename)
	content = text.readlines()
	text.close()

	z = float(content[-1].split()[2])
	
	#print(z)
	
	int3s2p[z] = 0
	int3d2p[z] = 0
	int2s2p[z] = 0
	int3p2s[z] = 0
	int3d2s[z] = 0
	int2p1s[z] = 0
	int3p1s[z] = 0
	int3d1s[z] = 0
	
	pop3s[z] = 0
	pop3p[z] = 0
	pop3d[z] = 0
	pop2s[z] = 0
	pop2p[z] = 0

	for i in range(len(content)-1):
		line = content[i].split()
		var = [line[0],line[1]]
		empty = ''
		initial = int(empty.join(var))
		
		var = [line[3],line[4]]
		empty = ''
		final = int(empty.join(var))
		#print(initial,final)
		
		if initial == 30 and final == 21: #3s-2p
			int3s2p[z] += float(line[7])
			pop3s[z] += float(line[6])
			
		if initial == 32 and final == 21: #3d-2p
			int3d2p[z] += float(line[7])
			pop3d[z] += float(line[6])
			
		if initial == 20 and final == 21: #2s-2p
			int2s2p[z] += float(line[7])
			pop2s[z] += float(line[6])
		
		if initial == 31 and final == 20: #3p-2s
			int3p2s[z] += float(line[7])
			pop3p[z] += float(line[6])
		
		if initial == 32 and final == 20: #3d-2s
			int3d2s[z] += float(line[7])
			pop3d[z] += float(line[6])
		
		if initial == 21 and final == 10: #2p-1s
			int2p1s[z] += float(line[7])
			pop2p[z] += float(line[6])
		
		if initial == 31 and final == 10: #3p-1s
			int3p1s[z] += float(line[7])
			pop3p[z] += float(line[6])
		
		if initial == 32 and final == 10: #3d-1s
			int3d1s[z] += float(line[7])
			pop3p[z] += float(line[6])

for File in os.listdir('intensities/stat/'):
	print('processing file ' + File)
	intensity(File)

lists = [int3s2p, int3d2p, int2s2p, int3p2s, int3d2s, int2p1s, int3p1s, int3d1s]

for i in lists:
	title = i['name']
	del i['name']
	plt.clf()
	plt.title(title + ' intensity')
	plt.scatter(i.keys(), i.values())
	#plt.savefig('test_plots/intensity/stat/' + title + '_stat_intensities')
	#plt.show()


poplist = [pop2s, pop2p, pop3d, pop3p, pop3s]

for i in poplist:
	title = i['name']
	del i['name']
	plt.clf()
	plt.title(title + ' population')
	plt.scatter(i.keys(), i.values())
	#plt.savefig('test_plots/intensity/stat/' + title + '_stat_population')
	#plt.show()
	print(i.keys())
