#!/usr/bin/env python
##########################################################################
# This file is part of d00ks.
# 
# d00ks is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# d00ks is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with d00ks.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################



from parser import *
from sys import argv

f = open(argv[-1])
prog = f.read()
output = parser.parse(prog)

for (label, line) in output:
	print "%s\t%s"%(label+"\n" if label else "", line if line else "")

program = simulator.Program()
program.compile(output)

if "-e" in argv:
	program.run()
else:
	program.debug()
