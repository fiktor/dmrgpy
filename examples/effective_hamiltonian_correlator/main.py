# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import spinchain
n = 6
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
e = sc.gs_energy()

#%dmrgpy: exclude_from_tests
# The following call to get_effective_hamiltonian returns LaTeX string
# representing the effective Hamiltonian, not a pair of matrices as
# expected by the code below.

# Now get the low energy Hamiltonian:
h, b = sc.get_effective_hamiltonian()
print(sc.get_excited(n=4))
import scipy.linalg as lg
print(np.round(lg.eigvalsh(b),3))
es,vs = lg.eigh(-b)
vs = vs.transpose()
print(vs[0].real)
print(np.round(lg.eigvalsh(h),3))

