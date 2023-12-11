// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_GET_RANDOM_MPS_H
#define __MPSCPP2_GET_RANDOM_MPS_H

#include "get_sites.h"

static auto get_random_mps = []() {
  // read the GS from a file
  auto sites = get_sites(); // Get the different sites
  auto psi = MPS(sites);
  writeToFile("random.mps", psi); // write to file
};
#endif // __MPSCPP2_GET_RANDOM_MPS_H
