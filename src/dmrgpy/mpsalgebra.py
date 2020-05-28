from . import mps
import numpy as np

def exponential(self,h,wf,mode="DMRG",**kwargs):
    if mode=="DMRG": return exponential_dmrg(self,h,wf,**kwargs)
    elif mode=="ED": return self.get_ED_obj().exponential(h,wf,**kwargs)
    else: raise


def exponential_dmrg(self,h,wfa,dt=1.0,nt=1000):
    """Compute the exponential of a wavefunction"""
    nt0 = int(self.bandwidth(h)*nt)
    task = {"exponential_eMwf":"true",
            "tevol_dt_real":str(-dt.real),
            "tevol_dt_imag":str(dt.imag),
            "tevol_n":str(nt0),
            }
    self.task = task # override tasks
    wfa.copy(name="input_wavefunction.mps") # copy wavefunction
    self.execute(lambda: h.write(name="hamiltonian.in"))
    self.execute(lambda : self.run()) # run calculation
    wf = mps.MPS(self,name="output_wavefunction.mps").copy() # output
    return wf

def overlap(self,wf1,wf2,mode="DMRG"):
    if mode=="DMRG": return overlap_dmrg(self,wf1,wf2)
    elif mode=="ED": return self.get_ED_obj().overlap(wf1,wf2)
    else: raise


def overlap_dmrg(self,wf1,wf2):
    """Compute the overlap between wavefunctions"""
    task = {"overlap":"true",
            }
    self.task = task # override tasks
    wf1.copy(name="overlap_wf1.mps") # copy wavefunction
    wf2.copy(name="overlap_wf2.mps") # copy wavefunction
    self.execute( lambda : self.run()) # run calculation
    m = self.execute( lambda : np.genfromtxt("OVERLAP.OUT")) # run calculation
    return m[0] + 1j*m[1]


def applyoperator(self,A,wf,mode="DMRG"):
    if mode=="DMRG": return applyoperator_dmrg(self,A,wf)
    elif mode=="ED": return self.get_ED_obj().applyoperator(A,wf)


def applyoperator_dmrg(self,A,wf):
    """Apply operator to a many body wavefunction"""
    task = {"applyoperator":"true",
            "applyoperator_wf0":wf.name,
            "applyoperator_multioperator":"applyoperator_multioperator.in",
            "applyoperator_wf1":"applyoperator_wf1.mps",
            }
    self.execute(lambda: A.write(name="applyoperator_multioperator.in"))
    self.task = task
    self.execute( lambda : self.run()) # run calculation
    return mps.MPS(self,name="applyoperator_wf1.mps").copy() # copy




