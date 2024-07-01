import angr

p = angr.Project('angr1')

state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)

# sm.run(until=lambda sm_: any([a.addr==0x4007b1 for a in sm_.active]))
sm.explore(find=0x4007a0)

found = sm.found[0]
ss = found.posix.dumps(0)
print("found input: ", repr(ss))

# input1_t1=possible_inputs[0].decode('utf-8')
input1_t1=ss
with open("input1_t1", "wb") as file:
	file.write(input1_t1)
