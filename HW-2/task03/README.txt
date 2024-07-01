Command to run:
python script.py

The binary is decompiled in Ghidra and analysed. We can see 2 functions, prompter and admin_checker. The prompter uses scanf function which takes user input. The function admin_checker doesn't take any input but checks a variable for value and if the variable has specific value, then reads and ouputs flag.

We debug the file using gdb and we notice that the memory at which the local variable is($rbp-0x12) can be written using the input given by the user. The if condition in admin_checker function checks if the variable is equal to '0x1337'.

We will design the input string such that the memory location(rbp-0x12) is written with value '0x1337'.

Since '0x13' is non printable character, the scripts uses the subprocess python library to interact with the binary and give bytes as input. 
