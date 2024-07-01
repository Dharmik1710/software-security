script.py and pwntools are used to interact with the process.

We notice that the memory is randomized, i.e stack is ramdomized. The code is decompiled in ghidra and we notice printf without formating is used to print the user input without sanitizing the input. We can use this printf to get the address of the buffer. r9 stores the address to the buffer. The input string is "rsi: %p rdx: %p rcx: %p r8: %p r9: %p stack: %p %p".

We will set the real user id to effective user if by getting the uid from /etc/passwd of the task03flag

There are two printfs in the code, the first printf is used to leak information about stack, i.e buffer address. We overflow the buffer of 115 bytes and overwrite the return address. The offset is 136 bytes which can be found by debugging the binary in debug mode. Hence our payload is Shellcode padded with '\xfe', such that total length is 136 bytes, followed by return address pointing to the start of the buffer.
