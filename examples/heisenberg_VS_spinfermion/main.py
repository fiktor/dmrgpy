# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import spinchain
from dmrgpy import spinfermionchain
n = 7
spins = [2 for i in range(n)] # spin 1/2 heisenberg chain
def geth(sc):
  h = 0
  for i in range(n-1): 
      h = h + sc.Sx[i]*sc.Sx[i+1]
      h = h + sc.Sy[i]*sc.Sy[i+1]
      h = h + sc.Sz[i]*sc.Sz[i+1]
  return h

sc = spinchain.Spin_Chain(spins)
sc.set_hamiltonian(geth(sc))
sc_energy0 = sc.gs_energy()

fc = spinfermionchain.Spin_Fermion_Hamiltonian(["S" for s in spins])
fc.set_hamiltonian(geth(fc))
fc_energy0 = fc.gs_energy()
fc_density = fc.get_density()

print("Energy with spins", sc_energy0)
print("Energy with fermions", fc_energy0)
print("Fermion density", fc_density)
