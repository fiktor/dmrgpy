// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_GET_EXCHANGE_H
#define __MPSCPP2_GET_EXCHANGE_H

#include "get_sites.h"

static auto get_exchange = [](auto ampo) {
  ifstream jfile;            // file to read
  jfile.open("exchange.in"); // file with the coupling
  int nj;
  jfile >> nj; // read the number of couplings
  std::complex<double> jxx, jxy, jxz, jyx, jyy, jyz, jzx, jzy, jzz;
  int j1, j2;    // indexes for the sites
  int c1, c2;    // indexes for the components
  auto tr = 0.0; // value
  auto ti = 0.0; // value
  auto name1 = "Sx";
  auto name2 = "Sx";
  for (int i = 0; i < nj; ++i) {
    jfile >> j1 >> j2 >> c1 >> c2 >> tr >> ti; // everything
    j1 += 1; // numbering in Itensor starts in 1
    j2 += 1; // same
    // both are spins
    if ((site_type(j1 - 1) != 1) and (site_type(j2 - 1) != 1)) {
      if (c1 == 0)
        name1 = "Sx";
      if (c1 == 1)
        name1 = "Sy";
      if (c1 == 2)
        name1 = "Sz";
      if (c2 == 0)
        name2 = "Sx";
      if (c2 == 1)
        name2 = "Sy";
      if (c2 == 2)
        name2 = "Sz";
      ampo += tr, name1, j1, name2, j2;
      ampo += ti * 1i, name1, j1, name2, j2;
    };
  };
  jfile.close();
  return ampo; // return the Hamiltonian with exchange added
};
#endif // __MPSCPP2_GET_EXCHANGE_H
