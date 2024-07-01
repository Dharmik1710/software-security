This is a classic example of ROP chaining

The stack is not executable but we can buffer overflow and point our return address to the ROP chain

By debugging using GBD, we can calculate the offset which is 56 bytes.

We can put any values up to 56 bytes, and then make return address point to our first gadget from the ROP chain, followed by the ROP chain.

We can find gadgets using ropper command.
ropper --file ./binary --search "pop rax; ret"

It may happen sometimes that we wouldn't be able to find the exact command that we want. For e.g. 
# mov qword ptr [rax], rdi; pop rbx; ret
ropp += p64(0x487804)
ropp += p64(0xcafecafe)

We can put some garbage value on the stack which will be poped and also this value should not be previouly set and used later.

I have used chmod systemcall which is very similar to open system call. The rax will be 90, rdi will be the pointer to the filename and rsi will be the permissions(for e.g. 0744) that you need to set for the file. Then the syscall is performed 