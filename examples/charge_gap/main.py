# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
import matplotlib.pyplot as plt
from dmrgpy import fermionchain
n = 6
fc = fermionchain.Fermionic_Chain(n) # create the chain
h = 0
for i in range(n-1):
    h = h + fc.C[i]*fc.Cdag[i+1]
for i in range(n-1):
    h = h + (fc.N[i]-.5)*(fc.N[i+1]-.5)

h = h + h.get_dagger()
fc.set_hamiltonian(h)
print("Many-body gap",fc.get_gap())
#%dmrgpy: exclude_from_tests
# As of 2023-12-06 the following line fails:
# manybodychain.Many_Body_Chain.to_origin() detects "/ERROR"
# after executing the task scheduled by
# manybodychain.Many_Body_Chain.multi_vev(...).
g = fc.get_charge_gap(d=2)
print("Charge gap",g)









