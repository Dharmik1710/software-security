This is an example of arbitrart memory read and memory write. Also the libc is randomized. But the GOT table is not randomized. We can arbitrary read, write and echo the user input as many times as we want.

Step by step process

1. We perform read operation to read the puts address in libc from GOT table by performing read operation on the fixed puts mapping in GOT table

2. We use GDB to calculate the offset between puts function and system function in libc

3. We can now calculate the address of system call in libc by subtracting the offset from the puts address

4. Now we will use arbitrary write to overwrite the puts address to system's address in GOT table

5. Now we will use echo function which uses puts function call, which will be fetched from GOT table

6. The function also get the user input, which we can give as "/bin/sh"

7. This will spawn a shell and then we can cat out the flag.