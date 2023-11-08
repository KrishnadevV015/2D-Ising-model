import numpy as np
import matplotlib.pyplot as plt
N=100
p=0.5

def initial_arrrangements(N,p):
    lattice1 = np.random.random(size=(N, N))
    lattice = np.zeros((N,N))    
    lattice[lattice1>=p] = 1
    lattice[lattice1<p] = -1
    return lattice

def nearest_neighbours(lattice,i,j):
    return  lattice[(i+1)%N,j]+lattice[(i-1)%N,j]+lattice[i,(j+1)%N]+lattice[i,(j-1)%N]

def Rearrange(lattice):
    beta=1
    for a in range(N):
        for b in range(N):
            i=np.random.randint(0,N)
            j=np.random.randint(0,N)
            sigma=lattice[i,j]
            del_E=2*sigma*nearest_neighbours(lattice,i,j)
            if del_E<0:
                sigma=-1*sigma
            elif np.random.rand()<np.exp(-del_E*beta):
                sigma=-1*sigma
            lattice[i,j]=sigma
    return lattice

plt.figure(figsize=(10,20))
lattice=initial_arrrangements(N,p)
plt.subplot(2,1,1)
plt.imshow(lattice)
plt.title('Initial arrangemet of lattice with initially 50% of the spins align up',fontsize=20)

plt.subplot(2,1,2)
for i in range(100):
    Rearrange(lattice)
plt.imshow(lattice)
plt.title('Arrangemet of lattice after 100 steps',fontsize=20)
plt.savefig('lattice.png',dpi=400)
plt.show()
