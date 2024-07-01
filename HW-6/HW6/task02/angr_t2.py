import angr
import claripy

class mm(angr.SimProcedure):
	def run(self, c):
		# c is already a bit vector
		ret = c + 4
		self.state.add_constraints(ret >= 4)
		self.state.add_constraints(ret <= 255)		
		print("input c: %s" % self.state.solver.eval(c))
		print("ret val: %s" % self.state.solver.eval(ret))
		return ret


p = angr.Project('angr2')
p.hook_symbol(0x4007a0, mm())
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)

sm.explore(find=0x400898)
found = sm.found[0]
ss = found.posix.dumps(0)
print("sm: ", sm)
print("found: ", found)
print("solution: ", repr(ss))

# sm.explore(find=0x400898)
# found = sm.found[0]
# ss = found.posix.dumps(0)
# print("found input: ", repr(ss))

# input1_t1=possible_inputs[0].decode('utf-8')
input1_t2=ss
with open("input1_t2", "wb") as file:
	file.write(input1_t2)
