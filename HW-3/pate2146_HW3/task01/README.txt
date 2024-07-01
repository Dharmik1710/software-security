Command:
python3 -c 'import sys; sys.stdout.buffer.write(b"a"*56 + b"\xf6\x11\x40\x00\x00\x00\x00\x00")' | ./carlyraejepsen

First, we decompile the code using Ghidra. The main function has a buffer, scanf function is called which gets input from the user and store it in the buffer of size 48. 

Also we will check whether the program code is randomized by using 'proc/`pgrep ./carlyraejepsen`/maps' and we notice that program code is not randomized in memory.

We can overflow the buffer and overwrite the return address of the main function. The executable has also got flag function. We can design the attack string such that the return address points to the flag function. 

The address in the command is written as per little endian. The buffer is 48 bytes followed by rbp which is 8 bytes and 8 bytes of return address(which points to flag function)
