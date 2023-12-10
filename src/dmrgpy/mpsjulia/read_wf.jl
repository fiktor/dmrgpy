# SPDX-License-Identifier: GPL-3.0-or-later


function save_mps(filename,psi)
	serialize(filename,psi)
end


function load_mps(filename)
  return deserialize(filename)
end

