# SPDX-License-Identifier: GPL-3.0-or-later
# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
import spinchain
n = 30
spins = [3 for i in range(n)] # spin 1/2 heisenberg chain
sc = spinchain.Spin_Chain(spins) # create the spin chain
sc.kpmmaxm = 10 # KPM max m
fo = open("DCF.OUT","w") # dynamical correlation function
for i in range(n): # loop over sites
  (xs,ys) = sc.get_spismj(n=1000,mode="DMRG",i=i,j=i)
  print("Doing",i)
  for (x,y) in zip(xs,ys):
    fo.write(str(i)+"  ")
    fo.write(str(x)+"  ")
    fo.write(str(y)+"\n")
  fo.flush()
fo.close()











