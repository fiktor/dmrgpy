# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import spinchain
ns = np.array(range(4,30,2))
es = []
n = 30
spins = [3 for i in range(n)] # spin 1 chain
sc = spinchain.Spin_Chain(spins) # create the chain
sc.set_hamiltonian(sum(
    Si[i] * Si[i + 1]
    for i in range(n - 1)
    for Si in [sc.Sx, sc.Sy, sc.Sz]))
pairs = [(i, i+1) for i in range(n-1)] # correlators
sc.gs_energy() # compute the correlator between these sites
cs = sc.get_correlator(pairs) # compute the correlator between these sites
import matplotlib.pyplot as plt
plt.plot(range(len(cs)),cs,marker="o") # correlator using DMRG
plt.show()











