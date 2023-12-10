# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import spinchain
def get(n):
  spins = ["S=1/2" for i in range(n)] # spin 1/2 heisenberg chain
  sc = spinchain.Spin_Chain(spins) # create the spin chain
  h = 0
  for i in range(n-1):
      h = h +sc.Sx[i]*sc.Sx[i+1]
      h = h +sc.Sy[i]*sc.Sy[i+1]
      h = h +sc.Sz[i]*sc.Sz[i+1]
  sc.set_hamiltonian(h)
  return sc


import time


def compare(n):
  t0 = time.time()
  sc = get(n)
  name = (sc.Sx[0],sc.Sx[0])
  sc.get_dynamical_correlator(name=name)
  t1 = time.time()
  sc = get(n)
  sc.setup_julia()
  #%dmrgpy: exclude_from_tests
  # This fails because get_dynamical_correlator uses is_hermitian check,
  # which relies on random_mps task, which is not implemented in Julia.
  sc.get_dynamical_correlator(name=name)
  t2 = time.time()
  return t1-t0,t2-t1


ns = [4,8,10,20]
f = open("TIMES.OUT","w")
for n in ns:
    dt0,dt1 = compare(n)
    f.write(str(n)+"  ")
    f.write(str(dt0)+"  ")
    f.write(str(dt1)+"\n")
    f.flush()
    print("Time with C++",dt0)
    print("Time with Julia",dt1)
    print()
f.close()

