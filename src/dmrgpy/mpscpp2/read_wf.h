// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_READ_WF_H
#define __MPSCPP2_READ_WF_H
// this does not work yet

auto read_wf(std::string name = "psi_GS.mps") {
  auto sites = get_sites();
  //  readFromFile("sites_file",sites);
  sites = get_sites();
  readFromFile("sites.sites", sites);
  auto psi = MPS(sites);
  readFromFile(name, psi);
  return psi;
}
#endif // __MPSCPP2_READ_WF_H
