class registers(object):
	def __init__(self):
		self.regs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.LR = 14
		self.PC = 15
		self.CPSR = 16
		
		self.N = 0x80000000
		self.Z = 0x40000000
		self.C = 0x20000000
		self.V = 0x10000000
		self.J = 0x02000000
		self.E = 0x00000200
		self.A = 0x00000100
		self.I = 0x00000080
		self.F = 0x00000040
		self.T = 0x00000020
		
		self.symbol_table = {}
		
		self.changed = []
	
	def __getitem__(self, key):
		return self.regs[key]
	
	
	def __setitem__(self, key, value):
		value = value & 0xFFFFFFFF
		if self.regs[key] != value:
			self.regs[key] = value
			self.changed.append(key)
		
	def symbol_insert(self, key, index, value):
		# TODO: symbol already exists error
		self.symbol_table[key] = (index, value)
	
	def symbol_abs(self, value):
		(i, val) = self.symbol_table[value]
		return i
		
	def flag_set(self, flag, value):
		if value:
			self.regs[self.CPSR] |= flag
		else:
			self.regs[self.CPSR] &= (~flag)
	
	def flag_get(self, flag):
		return 1 if self.regs[self.CPSR] & flag else 0
	
	def set_clean(self):
		self.changed = []
	
	def p(self):
		ret = "registers {\n"
		for i in range(0, len(self.regs)):
			ret += "%s	R%i = 0x%08X = %d\n"%("*" if i in self.changed else " ", i, self.regs[i], self.regs[i])
		ret += "} "
		ret += "N = %i, Z = %i, C = %i, V = %i"%(int(self.flag_get(self.N)), int(self.flag_get(self.Z)), int(self.flag_get(self.C)), int(self.flag_get(self.V)))
		print ret