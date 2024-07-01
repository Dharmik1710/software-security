The program takes first calculates the dd which in my case is 12992, which is multiplication of first and third character in username(i.e. p->112 and t->116). It is calculated using dd.c

The address of the buffer is printed out by the program.

The program gets the input and write into the memory. c is the user controlled input. If the (dd ^ 10 == c), then c is written to the memory; else if (c == 10), then 10 is written in the memory else (c ^ dd) is written to the memory. 

The maximum writable bytes into the memory is 168.

The program then checks if bytes corresponding to 'setreuid(geteuid(), geteuid())' is present in the memory that is written into the buffer. Also it checks if '/bin/sh' string is present with syscall('0xf') byte. If any of the conditions is true, it breaks and exits the program.

We need to craft the input string in such a way that it does not make use of syscall directly or syscall can also be encoded in such a way the final shell should not consists of 0xf bytes. We also need to make sure the code doesnot consists of '/bin/sh' string, i.e. '\x73' and '\x68' bytes should not be present. '\x62', '\x69', '\x6e', '\x73', '\x68' and '\xf' should not be present in the code.

The buffer is 140 bytes, 4 bytes of integer value and 8 bytes saved rbp. Hence the offset is 152. The return address can be overwritten to point to the start of the buffer where the exploit is stored.
