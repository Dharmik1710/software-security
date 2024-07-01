This is very similar to the previous task(task02).

I have used the same ROP chain.

The function reads upto 512 bytes from the user and waits for the user to send that many number of bytes. If the number is greater than 512, it exits. The buffer is also of 512 bytes. 

There is a canary check, although we may need not know the value, because there is a function call before that and we can exploit the return address of the call by over writing it.

We can overflow integer as the expected input is signed integer while the comparison is done by converting to signed integer

We can pass negative integer through which we can potentially pass the buffer of more than 512 bytes and overwrite the return address to initiate ourto ROP chain

The exploit string is designed as ROP chain, followed by padding of some value to reach the return address(rop + padding = 512 bytes), overwriting the return address with our first gadget and followed by padding of some values upto the total size of the buffer expected.

We need to modify our ROP chain because using GDB we notice that the user controlled input is 3 pops in the stack, so we initiate the ROP chain by poping 3 times for it to actually reach or ROP chain