import numpy as np
import matplotlib.pyplot as plt

A = 0.2 # A/e
xi = 2 # xi/sigma
alpha = 50

def V(r):
    return 4*((1/r)**(2*alpha) - (1/r)**alpha) + A*np.exp(-r/xi)/(r/xi)

rlist = np.logspace(-1,2,500) 
#rlist = np.logspace(0.3,2,500) # 遠距離

plt.plot(rlist,V(rlist),ls='-')
plt.plot(rlist,A/rlist,ls='--')
plt.plot(rlist,4*(1/rlist)**(2*2),ls=':')
plt.plot(rlist,-4*(1/rlist)**2,ls=':')
plt.xscale('log')
#plt.yscale('log') # 遠距離用．エネルギー負の部分が削れるので注意

#plt.xlim(0.5,2)
plt.ylim(-2,2)

plt.xlabel(r'$r/\sigma$')
plt.ylabel(r'$V(r)/e$')
plt.show()