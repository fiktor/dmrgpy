# SPDX-License-Identifier: GPL-3.0-or-later
import Dates
function main()
	if get_bool("GS") # ground state energy
		get_gs()
	end
	if get_bool("vev") # vacuum expectation value
		get_vev()
	end
	if get_bool("write_sites") # vacuum expectation value
		get_sites()
	end
	if get_bool("many_vev") # vacuum expectation value
		get_many_vev()
	end
	if get_bool("dynamical_correlator") # vacuum expectation value
		dynamical_correlator_kpm()
	end
	if get_bool("applyoperator") # apply an operator
		applyoperator()
	end
	if get_bool("general_kpm") # apply an operator
		general_kpm()
	end
	if get_bool("overlap") # apply an operator
		overlap()
	end
	if get_bool("summps") # sum two mps
		summps()
	end
	if get_bool("exponential_eMwf") # apply an operator
		exponential()
	end
  now_str = Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS")
  println("MatrixProductStates.main completed @ $(now_str).")
end
