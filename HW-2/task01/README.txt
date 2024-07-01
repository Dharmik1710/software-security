Command:
./ez_rev qisXIzlVkOcBQlGDSEwj


We will decompile the binary using Ghidra and analyse the file using the default options. 

You can see the decompiled code and the assembly program in Ghidra. The main function consists if conditions. 2 parameters are expected, and the second parameter is expected of lenght 20. There is one flag which calls check_flag function which if returns 1, then the flag is read. 

The function has if condition and which expects the input in specific format. The script.py calculates the expected input, which is 'qisXIzlVkOcBQlGDSEwj'.
