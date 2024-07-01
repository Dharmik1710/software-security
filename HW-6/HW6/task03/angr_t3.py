import angr

p = angr.Project('angr1')

state = p.factory.entry_state()
sm = p.factory.simulation_manager(state, auto_drop=["deadended"])

sm.step()

# sm.run(until=lambda sm_: any([a.addr==0x4007b1 for a in sm_.active]))

while len(sm.active)>=1:
	sm.step()
	print(sm)
	if(len(sm.unconstrained) > 0):
		break

ucstate = sm.unconstrained[0]

print("rip(uc state): ", ucstate.regs.rip)
ss = ucstate.posix.dumps(0)
print("concrete input: ", ss)



# sm.explore(find=0x4007a0)

# found = sm.found[0]
# ss = found.posix.dumps(0)
print("seg fault input: ", repr(ss))

input1_t3=ss
with open("input1_t3", "wb") as file:
	file.write(input1_t3)