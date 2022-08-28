''' - calculates maximum n value for given z
	- computes l population distribution'''

import numpy as np
import matplotlib.pyplot as plt
import math

zvalue = 18 #input z value z = 18 - Ar

def n(Z):
	return math.sqrt((Z*(1+2*math.sqrt(Z)))/(1+2/math.sqrt(Z)))

maxn = n(zvalue)	
print('maxn =', maxn)

maxn = 11

def CSq(n,l):
	if l == 0:
		return 1/n
		
	else:
		CPrevious = CSq(n,l-1)
		return CPrevious * ((2*(l-1)+3)/(2*(l-1)+1)) * ((n-1-(l-1))/(n+1+(l-1)))
		
		
def CSqContinuous(n,l):
	if l>=n:
		return 1
	return (2*l+1)*(math.gamma(n)**2)/math.gamma(n-l)/math.gamma(n+l+1)
	
print('CSq')
			
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

print(sum(Pvalues.values()))

print('')
print('CSqContinuous')
print('')

#~ nvalues = [(n*19)/(maxn) for n in range(1, maxn+1)]
nvalues = np.linspace(1,19,maxn)
print(nvalues)

for n in nvalues:
	Cs = [CSqContinuous(n,l) for l in Llist]
	
Csum = sum(Cs)

def P(n,l):
	return CSqContinuous(n,l)/Csum
	
Pvalues = {}
Llist = [l for l in range(maxn)]

for l in Llist:
	p = P(maxn,l)*100
	Pvalues[l] = p
	
s = sum(Pvalues.values())
	
for i in range(len(Pvalues.values())):
	Pvalues[i] /= s/100	
	
print(Pvalues)

print(sum(Pvalues.values()))






