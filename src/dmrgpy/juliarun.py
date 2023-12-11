# SPDX-License-Identifier: GPL-3.0-or-later
# routines to run the code with Julia
import os
import subprocess
import sys
import functools

DMRG_PATH = os.path.dirname(os.path.realpath(__file__))

START_JULIA = f"""
import Dates;
println(
    "Starting 'instantiate' @ ",
    Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"));
flush(stdout);
juliamps_dir = joinpath("{DMRG_PATH}", "julia", "MatrixProductStates");
import Pkg;
Pkg.activate(juliamps_dir);
Pkg.instantiate();
import MatrixProductStates;
"""

@functools.cache
def get_jlsession():
    class JuliaCallSession:
        def __init__(self):
            import juliacall
            jl = self.jlsession = juliacall.newmodule("dmrgpy")
            julia_dir = os.path.join(DMRG_PATH, "julia", "MatrixProductStates")
            for line in START_JULIA.split(";\n"):
                jl.seval(line)
        def main(self):
            return self.jlsession.MatrixProductStates.main()

    # The following may raise an exception.
    # We do not catch it, because we do not have other ways to run Julia.
    return JuliaCallSession()

def run(obj):
    """Execute mpsjulia.jl"""
    obj.execute(get_jlsession().main)


def install():
    """Install Julia and ITensor"""
    julia = "julia" # julia command
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"ITensors\\\")\"")
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"PyCall\\\")\"")
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"Suppressor\\\")\"")
    precompile()


def precompile():
    """Precompile Julia"""
    julia = "julia" # julia command
    os.system(julia+" --eval  \"using ITensors; ITensors.compile()\"")

