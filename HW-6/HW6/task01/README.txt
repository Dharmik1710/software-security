For this task, I have used angr to print out an "EASTER EGG".

The python script angr_t1.py performs symbolic execution on binary angr1 and stores the output to print easter egg to input1_t1 file.

Following are the steps used
1. First load our binary into angr, initializa the state and create a simulation manager
2. Use gdb or ghidra to get the address of the instruction that prints easter egg to stdout
3. Use explore function to step and continue until the required instruction is reached and executed by simulation manager
4. Get the concrete input formed from the constraints using posix.dumps
5. Store the input in the file input1_t1
6. Pass the required input to binary and the easter agg is printed out

Command : cat input1_t1 | ./angr1