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
int3d1s = {}
int3d1s['name'] = '3d-1s'
int2p1s['thesis points'] = {'z':[18,36], 'int':[0.8960, 0.8803]}#stat
#~ int2p1s['thesis points'] = {'z':[18,36], 'int':[0.4333, 0.6071]}#transfer
int3p1s = {}
int3p1s['name'] = '3p-1s'
int3p1s['thesis points'] = {'z':[18,36], 'int':[0.0389, 0.0523]}#stat
#~ int3p1s['thesis points'] = {'z':[18,36], 'int':[0.0933, 0.1015]}#transfer
int4p1s = {}
int4p1s['name'] = '4p-1s'
int4p1s['thesis points'] = {'z':[18,36], 'int':[0.0111, 0.0118]}#stat
#~ int4p1s['thesis points'] = {'z':[18,36], 'int':[0.0595, 0.0352]}#transfer
int5p1s = {}
int5p1s['name'] = '5p-1s'
int5p1s['thesis points'] = {'z':[18,36], 'int':[0.0126, 0.0048]}#stat
#~ int5p1s['thesis points'] = {'z':[18,36], 'int':[0.0843, 0.0194]}#transfer
int6p1s = {}
int6p1s['name'] = '6p-1s'
int6p1s['thesis points'] = {'z':[18,36], 'int':[0.0134, 0.0040]}#stat
#~ int6p1s['thesis points'] = {'z':[18,36], 'int':[0.0924, 0.0181]}#transfer
int7p1s = {}
int7p1s['name'] = '7p-1s'
int7p1s['thesis points'] = {'z':[36], 'int':[0.0027]}#stat
#~ int7p1s['thesis points'] = {'z':[36], 'int':[0.0189]}#transfer
int8p1s = {}
int8p1s['name'] = '8p-1s'
total1s = {}
#~ total1s['name'] = 'total'


file_location = 'intensities/full_shell/stat/'

def intensity(filename):
	text = open(file_location + filename)
	content = text.readlines()
	text.close()

	z = float(content[-1].split()[2])
	
	#print(z)
	
	total1s[z] = 0

	int3s2p[z] = 0 
	int3d2p[z] = 0
	int2s2p[z] = 0
	int3p2s[z] = 0
	int3d2s[z] = 0
	int2p1s[z] = 0
	int3p1s[z] = 0
	int3d1s[z] = 0
	int4p1s[z] = 0
	int5p1s[z] = 0
	int6p1s[z] = 0
	int7p1s[z] = 0
	int8p1s[z] = 0

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
			
		elif initial == 32 and final == 21: #3d-2p
			int3d2p[z] += float(line[7])
						
		elif initial == 20 and final == 21: #2s-2p
			int2s2p[z] += float(line[7])
		
		elif initial == 31 and final == 20: #3p-2s
			int3p2s[z] += float(line[7])
		
		elif initial == 32 and final == 20: #3d-2s
			int3d2s[z] += float(line[7])
			
		elif initial == 32 and final == 10: #3d-1s
			int3d1s[z] += float(line[7])
		
		elif initial == 21 and final == 10: #2p-1s
			int2p1s[z] += float(line[7])
			total1s[z] += float(line[7])
		
		elif initial == 31 and final == 10: #3p-1s
			int3p1s[z] += float(line[7])
			total1s[z] += float(line[7])
		
		elif initial == 41 and final == 10: #4p-1s
			int4p1s[z] += float(line[7])
			total1s[z] += float(line[7])
			
		elif initial == 51 and final == 10: #5p-1s
			int5p1s[z] += float(line[7])
			total1s[z] += float(line[7])
			
		elif initial == 61 and final == 10: #6p-1s
			int6p1s[z] += float(line[7])
			total1s[z] += float(line[7])
			
		elif initial == 71 and final == 10: #7p-1s
			int7p1s[z] += float(line[7])
			total1s[z] += float(line[7])
			
		elif initial == 81 and final == 10: #8p-1s
			int8p1s[z] += float(line[7])
			total1s[z] += float(line[7])
			
	#~ print(total)
					

def plot(intensity):
	title = intensity['name']
	del intensity['name']
	
	delete = []
	
	for i in intensity:
		if intensity[i] == 0:
			delete.append(i)
			
	for i in delete:
		del intensity[i]
		
	plt.clf()
	
	try:
		thesis = intensity['thesis points']
		plt.scatter(thesis['z'], thesis['int'], marker = 's', c = 'tab:orange', label = 'thesis')
		del intensity['thesis points']
		
	except:
		pass
		
	
	plt.title(title + ' full shell capture intensity')
	plt.scatter(intensity.keys(),intensity.values(), label = 'calculated')
	plt.ylim((0,1))
	plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1],[0, 20, 40, 60, 80, 100])
	plt.xlabel('Z')
	plt.ylabel('Intensity (%)')
	plt.legend()
	plt.savefig('plots/intensity/full_shell/capture_' + title + '_full_shell_intensity.png')
	#~ plt.show()
	

for File in os.listdir(file_location):
	print('processing file ' + File)
	intensity(File)

#~ dicts = [int3s2p, int3d2p, int2s2p, int3p2s, int3d2s, int2p1s, int3p1s, int3d1s, int4p1s, int5p1s, int6p1s, int7p1s, int8p1s]
dicts = [int2p1s, int3p1s, int4p1s, int5p1s, int6p1s, int7p1s, int8p1s]

for d in dicts:
	plot(d) #individual transitions

#all transitions to 1s		
plt.clf()
plt.title('full shell p-1s capture intensity')
plt.scatter(int2p1s.keys(), int2p1s.values())
plt.scatter(int3p1s.keys(), int3p1s.values())
plt.scatter(int4p1s.keys(), int4p1s.values())
plt.scatter(int5p1s.keys(), int5p1s.values())
plt.scatter(int6p1s.keys(), int6p1s.values())
plt.scatter(int7p1s.keys(), int7p1s.values())
plt.scatter(int8p1s.keys(), int8p1s.values())
#~ plt.scatter(total1s.keys(), total1s.values())
plt.ylim((0,1))
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1],[0, 20, 40, 60, 80, 100])
plt.xlabel('Z')
plt.ylabel('Intensity (%)')
plt.legend(['2p-1s', '3p-1s', '4p-1s', '5p-1s', '6p-1s', '7p-1s', '8p-1s', 'total'])
plt.savefig('plots/intensity/full_shell/capture_full_shell_p-1s_intensity.png')
#~ plt.show()

#~ print(total1s)

#total transitions from 8p-2p to 1s
plt.clf()
plt.title('full shell total -1s capture intensity')
plt.scatter(total1s.keys(), total1s.values(), label = 'calculated')
plt.ylim((0,1))
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1],[0, 20, 40, 60, 80, 100])
plt.xlabel('Z')
plt.ylabel('Intensity (%)')
plt.legend()
plt.savefig('plots/intensity/full_shell/capture_full_shell_total_1s_intensity.png')
#~ plt.show()


intn1s = {}

for i in total1s.items():
	intn1s[i[0]] = 1 - i[1]
	
#np - 1s
plt.clf()
plt.title('full shell n-1s capture intensity')
plt.scatter([18, 36], [0.0237, 0.0388], marker = 's', c = 'tab:orange', label = 'thesis')#stat
#~ plt.scatter([18, 36], [0.2188, 0.2234], marker = 's', c = 'tab:orange', label = 'thesis')#transfer
plt.scatter(intn1s.keys(), intn1s.values(), label = 'calculated')
plt.ylim((0,1))
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1],[0, 20, 40, 60, 80, 100])
plt.xlabel('Z')
plt.ylabel('Intensity (%)')
plt.legend()
plt.savefig('plots/intensity/full_shell/capture_full_shell_n-1s_intensity.png')
#~ plt.show()








