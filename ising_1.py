import numpy as np
import pandas as pd
 
p=0.25
N=20
step=2000
eqstep=300

def init(N,p):
    lattice1 = np.random.random(size=(N, N))
    lattice = np.zeros((N,N))    
    lattice[lattice1>=p] = 1
    lattice[lattice1<p] = -1
    return lattice


def nearest_neighbours(lattice,i,j):
    return  lattice[(i+1)%N,j]+lattice[(i-1)%N,j]+lattice[i,(j+1)%N]+lattice[i,(j-1)%N]

def energy(lattice,N):
    Te=0
    for i in range(N):
        for j in range(N):
            S=lattice[i,j]
            
            Te+=-S*nearest_neighbours(lattice,i,j)
    return Te/2
def magnetisation(lattice):
    return np.sum(lattice)


def mc_step(lattice,temp):
    beta=1/temp
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


def mc_step1(lattice,temp):
    beta=1/temp
    for a in range(N):
        for b in range(N):
            i=np.random.randint(0,N)
            j=np.random.randint(0,N)
            sigma=lattice[i,j]
            nb=lattice[(i+1)%N,j]+lattice[(i-1)%N,j]+lattice[i,(j+1)%N]+lattice[i,(j-1)%N]
            del_E=2*sigma*nb
            if del_E<0:
                sigma=-1*sigma
            elif np.random.rand()<np.exp(-del_E*beta):
                sigma=-1*sigma
            lattice[i,j]=sigma
    return lattice


def calcul(lattice,N,step,eqstep):
    T=np.linspace(1,6,50)    
    energies=[]
    magnet=[]
    specificheat=[]
    suscept=[]
    for t in T:
        E=0
        M=0
        E_sqr=0
        M_sqr=0
        for k in range(eqstep):
                mc_step(lattice,t)
        for i in range(step):
            mc_step(lattice,t)
            e=energy(lattice,N)
            m=magnetisation(lattice)
            E+=e
            M+=m
            E_sqr+=e**2
            M_sqr+=m**2
        E_mean=E/step
        M_mean=M/step
        E_sqrd_mean=E_sqr/step
        M_sqrd_mean=M_sqr/step
        Energy=E_mean/(N**2)
        MAgnetisation=M_mean/(N**2)
        specheat=(E_sqrd_mean-E_mean**2)/(N**2*t**2)
        SUCs=(M_sqrd_mean-M_mean**2)/(N**2*t)
        energies.append(Energy)
        magnet.append(MAgnetisation)
        specificheat.append(specheat)
        suscept.append(SUCs)
    data=pd.DataFrame({'T':T,'E':energies,'M':magnet,'Specific heat':specificheat,'Susceptib':suscept})
    data.to_csv('ising_{}_{}_check.csv'.format(p,N),index=False)
   
lattice=init(N,p)
calcul(lattice,N,step,eqstep)     