// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_BANDWIDTH_H
#define __MPSCPP2_BANDWIDTH_H

#include "get_gs.h"
#include "get_sweeps.h"

auto minimum_energy = [](auto sites, auto H) {
  static int called = 0;          // check if the function has been called
  static double saved_mine = 0.0; // minimum energy
  if (called == 0) {
    auto emin = get_gs_energy(H); // get the Hamiltonian
    saved_mine = emin;            // saved energy
    called = 1;                   // called
  };
  return saved_mine; // return energy
};

auto maximum_energy = [](auto sites, auto H) {
  // TODO: static variables are problematic here if we have
  // more than one Hamiltonian.
  static int called = 0;          // check if the function has been called
  static double saved_maxe = 0.0; // minimum energy
  if (called == 0) {
    auto psi = MPS(sites);      // initialize
    auto sweeps = get_sweeps(); // get the sweeps
    auto emax = -dmrg(psi, -1 * H, sweeps, {"Quiet=", true});
    saved_maxe = emax; // saved energy
    called = 1;        // called
  };
  return saved_maxe; // return energy
};

// scale the Hamiltonian so it lies between -1 and 1
static auto bandwidth = [](auto sites, auto H) {
  auto emin = minimum_energy(sites, H);
  auto emax = maximum_energy(sites, H);
  return emax - emin; // return the bandwidth
};
#endif // __MPSCPP2_BANDWIDTH_H
