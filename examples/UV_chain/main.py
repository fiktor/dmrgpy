# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import fermionchain
n = 4 # number of spinful fermionic sites
fc = fermionchain.Spinful_Fermionic_Chain(n) # create the chain
h = 0
for i in range(n-1): # hopping
    h = h + fc.Cdagup[i]*fc.Cup[i+1]
    h = h + fc.Cdagdn[i]*fc.Cdn[i+1]
for i in range(n): # Hubbard
    h = h + (fc.Nup[i]-.5)*(fc.Ndn[i]-.5)
for i in range(n-1): # V-interaction
    h = h + (fc.Nup[i]+fc.Ndn[i])*(fc.Nup[i+1]+fc.Ndn[i+1])
h = h + h.get_dagger()
##############################
# Setup the Many Body Hamiltonian
fc.maxm = 40
fc.nsweeps = 40
fc.set_hamiltonian(h) # set the hoppings
print(fc.gs_energy(mode="DMRG"))
print(fc.gs_energy(mode="ED"))
