''' - calculates maximum n value for given z
	- computes l population distribution
	- plots theoretical dist graph for cascades for given z'''

import numpy as np
import matplotlib.pyplot as plt
import math

zvalue = 12 #input z value z = 18 - Ar

def n(Z):
	return math.sqrt((Z*(1+2*math.sqrt(Z)))/(1+2/math.sqrt(Z)))


maxn = n(zvalue)	
print('maxn =', maxn)

maxn = 8

def CSq(n,l):
	if l == 0:
		return 1/n
		
	else:
		CPrevious = CSq(n,l-1)
		return CPrevious * ((2*(l-1)+3)/(2*(l-1)+1)) * ((n-1-(l-1))/(n+1+(l-1)))
				
Nlist = [n for n in range(1,maxn + 1)]
Llist = [l for l in range(len(Nlist))]

for n in Nlist:
	Cs = [CSq(n,l) for l in Llist]
	
Csum = sum(Cs)

def P(n,l):
	return CSq(n,l)/Csum
	
Pvalues = {}
Llist = [l for l in range(maxn)]

for l in Llist:
	p = P(maxn,l)*100
	Pvalues[l] = p
	
print(Pvalues)

for n in Nlist: #prints l pop values and generates plots
	for l in Llist:
		p = P(n,l)*100
		Pvalues[l] = p
		
	#plt.hist2d(Pvalues.keys(), Pvalues.values())
	#plt.title('l dist for n = ' + str(n))
	#plt.colorbar()
	#plt.show()
	#print('l dist for n = ' + str(n))
	#print(Pvalues)

def cumulative(func):
	count = 0
	r = np.random.random()
	while r > 0:
		r -= func(count)
		count += 1
		
	return count
	
functions = []

for n in Nlist:
	f = lambda l: P(n,l)
	functions.append(f)
	
x = []
y = []

print(len(functions))

#for i in range(200000): #generates cascade plot
	#n = int(np.random.random()*10)+1
	#x.append(cumulative(functions[n-1]))
	#y.append(n)
	
#plt.clf()
#plt.hist2d(x,y)
#plt.xlabel('l')
#plt.ylabel('n')
#plt.title('Theoretical dist for Z = ' + str(zvalue))
#plt.colorbar()
#plt.show()



