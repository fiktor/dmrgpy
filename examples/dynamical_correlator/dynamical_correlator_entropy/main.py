# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../../src')

import numpy as np
from dmrgpy import spinchain
from dmrgpy import entropy
import matplotlib.pyplot as plt

n = 10
spins = [2 for i in range(n)]
sc = spinchain.Spin_Chain(spins)

# We use bond-alternating XXZ model:
Jprime = 1.3
delta = 2.0
h = 0
for i in range(n-1):
    cur_J = Jprime if i % 2 == 0 else 1.0
    h += cur_J * (
        sc.Sx[i] * sc.Sx[i + 1]
        + sc.Sy[i] * sc.Sy[i + 1]
        + delta * sc.Sz[i] * sc.Sz[i + 1])
sc.set_hamiltonian(h)

sc.kpmmaxm = 40
# This is necessary for KPM_ENTROPY.OUT to be created,
# which is read by entropy.dynamical_correlator_kpm below:
sc.kpm_accelerate = False
x2, y2 = sc.get_dynamical_correlator(
    n=600, mode="DMRG", name=[sc.Sz[5], sc.Sz[5]], delta=0.02)
s = entropy.dynamical_correlator_kpm(sc)
plt.plot(range(len(s)), s, c="blue", label="DMRG")
plt.show()
