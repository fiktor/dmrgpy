# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import spinchain

def get(u):
    n = 16
    spins = ["S=1/2" for i in range(n)] # spin 1/2 heisenberg chain
    sc = spinchain.Spin_Chain(spins) # create the spin chain
    h = 0
    for i in range(n-1):
        h = h +sc.Sx[i]*sc.Sx[i+1]
        h = h +sc.Sy[i]*sc.Sy[i+1]
        h = h +sc.Sz[i]*sc.Sz[i+1]
    
    sc.set_hamiltonian(h)
    from dmrgpy import algebra ; algebra.maxsize = 70000
    #print(sc.get_excited(n=1,mode="ED")) ; exit()
    e = sc.gs_energy() # compute the ground state energy
    print("Energy",e)

from dmrgpy import parallel
parallel.cores = 4
parallel.pcall(get,range(4))









