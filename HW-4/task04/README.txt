Canary:  b'\x001\xc0\xe2W\xf2\x13\xfb'


This is an example of forking server.

We will brute force the canary as the server forks and creates the child process, which can be potentially buffer overflowed. For each connection, the canary value will not change.

The stack is executable

We can notice that the buffer is 40 bytes. Also we get the Ding message if the canary was preserved. If the canary is destroyed, we the connection is terminated

We will brute force the canary one byte by one byte.

Once the canary is retrieved, we will overflow the buffer and without changing the canary overwrite the retrun address of the function. The stack is randomized and there is no memory leak to obtain the stack address. We can notice one function yeet which contains a 'jmp [rsp]' instruction. Code is not randomized, so we can point our code to this instruction. 

Also I have used shellcraft get the exploit code. The exploit will open and listen for connection from a tcp port(1338) and will give a reverse shell when we connect to it.

As the exploit is more than 40 bytes, we will not be able to write it in the start of the buffer. We can write after the return address and as the 'jmp [rsp]' will point to after the return address.

Once the port is opened we can connect to the port and get the flag.