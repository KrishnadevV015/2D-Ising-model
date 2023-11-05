import numpy as np
import matplotlib.pyplot as plt

N=20
p=0.25

def magnetisation(lattice):
    return np.sum(lattice)

def nearest_neighbours(lattice,i,j):
    return  lattice[(i+1)%N,j]+lattice[(i-1)%N,j]+lattice[i,(j+1)%N]+lattice[i,(j-1)%N]

def init(N,p):
    lattice1 = np.random.random(size=(N, N))
    lattice = np.zeros((N,N))    
    lattice[lattice1>=p] = 1
    lattice[lattice1<p] = -1
    return lattice

def mc_step(lattice):
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

def magnetisation(lattice):
    return np.sum(lattice)

def nearest_neighbours(lattice,i,j):
    return  lattice[(i+1)%N,j]+lattice[(i-1)%N,j]+lattice[i,(j+1)%N]+lattice[i,(j-1)%N]

M=[]
n_steps=[]
lattice=init(N,p)
for i in range(500):
    n_steps.append(i)
    mc_step(lattice)
    M.append(magnetisation(lattice)/N**2)

plt.plot(n_steps,M)
plt.xlabel('Number of steps',fontsize=14)
plt.ylabel('Magnetisation',fontsize=14)
plt.show()
