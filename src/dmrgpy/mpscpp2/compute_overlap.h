// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_COMPUTE_OVERLAP_H
#define __MPSCPP2_COMPUTE_OVERLAP_H

#include "read_wf.h"

static auto compute_overlap = []() {
  ofstream myfile;
  auto wf1 = read_wf("overlap_wf1.mps"); // read first wavefunction
  auto wf2 = read_wf("overlap_wf2.mps"); // read second wavefunction
  auto out = overlapC(wf1, wf2);         // compute overlap
  myfile.open("OVERLAP.OUT");
  myfile << std::setprecision(20) << real(out) << endl; // compute
  myfile << std::setprecision(20) << imag(out) << endl; // compute
};
#endif // __MPSCPP2_COMPUTE_OVERLAP_H
