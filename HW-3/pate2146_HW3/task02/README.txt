script.py interacts with the process by using pwntools.

The program prints out the address of the buffer. The buffer is 128 bytes and the offset is 136. We can find the offset by using test string as input and getting the segmentation fault. 128 bytes of buffer, which is followed by 8 bytes of saved rbp and finally the return address pointing to the next instruction in the program. We exploit the function that gets the input from the user and returns.

The real user id is set to effective user id. The payload is shellcode, padded by '\xfe' bytes making the total of 136 bytes and finally followed by the address pointing to the start of buffer(overwriting the return address).
