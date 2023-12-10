# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../../src')

import numpy as np
from dmrgpy import spinchain
n = 6 # number of sites in the chain
spins = [2 for i in range(n)] # S=1/2
sc = spinchain.Spin_Chain(spins) # create the chain

# create two Hamiltonians
h0 = 0
h1 = 0
for i in range(n):
    h0 = h0+(-1)**i*sc.Sz[i]
for i in range(n-1):
    h1 = h1+sc.Sx[i]*sc.Sx[i+1] + sc.Sy[i]*sc.Sy[i+1] + sc.Sz[i]*sc.Sz[i+1] 


sc.set_hamiltonian(h0) # set AF hamiltonian
wf = sc.get_gs() # compute ground state
wfED = sc.get_gs(mode="ED") # compute ground state with ED
sc.set_hamiltonian(h1) # set the (new) Heisenberg Hamiltonian

from dmrgpy import timedependent
op = sc.Sz[0] # operator to compute

nt = 1e3 # number of time steps
dt = 1e-2 # time step
(ts,sz) = timedependent.evolve_and_measure(sc,operator=op,nt=nt,dt=dt,wf=wf)
(tsED,szED) = timedependent.evolve_and_measure(sc,
        operator=op,nt=nt,dt=dt,wf=wfED,mode="ED")

# now plot the result
import matplotlib.pyplot as plt
plt.plot(ts,sz.real,label="DMRG",c="blue")
plt.scatter(tsED,szED.real,label="ED",c="red")
plt.legend()
plt.show()











