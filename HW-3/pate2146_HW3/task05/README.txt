The program is 32-bit ALSR enabled binary. We need to change the context of out architecture to 'i386'.

The program reads input from the standard input and stores in the local buffer of 132 bytes. 

The ASLR is on for this binary and we control the environment variables, hence we need to brute force the address on the stack which points to the environment variable. You can use process routine of pwntools to pass the environment variables. Each variable has a limit of about 0.1MB, i.e. approximately 100,000B. We need much bigger space with NOPs in order to increase the window size of our randomly guessing the return address, we can create more environment variables.

We can use shellcraft from pwntools to write the 32-bit shell code, since its a 32-bit executable binary.

We can place the NOP sleds as large as approximately 1.7MB in the environment variable and try bruteforcing to find the required address to point to. As it a 32-bit, bruteforcing on the memory address space with huge NOPs seems doable. 

The shell code is at the end of the NOP sleds.

The payload will overflow the buffer and we can overwrite the return address to point to a random location in the stack. We know that stack always is at the higher addresses. Hecne we can point our return address to 0xff followed by 3 random bytes, since its a 32-bit binary.

If we run our script for about 10 times, since the stack is randomised, and the environments variables on stack occupy a huge chunk of the memory, there is a very good change that your return address points to NOP and sled down and the shell code is executed.


