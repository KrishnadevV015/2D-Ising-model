import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

file=pd.read_csv('ising data.csv',skiprows=0)

temp=file.iloc[:,0]
E=file.iloc[:,1]
M=file.iloc[:,2]
Cv=file.iloc[:,3]
X=file.iloc[:,4]

x1,y1=temp[9:15],M[9:15]

def line(x,m,c):
    return m*x+c

params, covm=curve_fit(line,y1,x1)
m=params[0]
c=params[1]
Tc=c
Threesigma=3*np.sqrt(covm[1][1])

plt.figure(1)
plt.plot(temp,E,'r*-')
plt.xlabel('Temperature ($J/k_b$)',fontsize=14)
plt.ylabel('Average Energy per Spin',fontsize=14)
plt.title('Average Energy V/S Temperature',fontsize=16)
plt.savefig('evst.png',dpi=400)

plt.figure(2)
plt.plot(temp,M,'b*-')
plt.xlabel('Temperature ($J/k_b$)',fontsize=14)
plt.ylabel('Average Magnetisation per spin',fontsize=14)
plt.title('Average Magnetisation V/S Temperature',fontsize=16)
plt.plot(line(y1,m,c),y1,'k',label='Fit given to find $T_c$')
plt.text(3,.5,'$T_c={}\pm{} J/k_B$'.format(round(Tc,2),round(Threesigma,2)))
plt.legend()
plt.savefig('mvst.png',dpi=400)

plt.figure(3)
plt.plot(temp,Cv,'k*-')
plt.xlabel('Temperature ($J/k_b$)',fontsize=14)
plt.ylabel('Specific heat',fontsize=14)
plt.title('Specific heat V/S Temperature',fontsize=16)
plt.savefig('cvvst.png',dpi=400)

plt.figure(4)
plt.plot(temp,X,'g*-')
plt.xlabel('Temperature ($J/k_b$)',fontsize=14)
plt.ylabel('Susceptibility',fontsize=14)
plt.title('Susceptibility V/S Temperature',fontsize=16)
plt.savefig('chivst.png',dpi=400)
plt.show()
