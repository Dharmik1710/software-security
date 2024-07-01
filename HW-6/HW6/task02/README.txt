For this task, I have used SimProcedure to find the input that prints "EASTER EGG!".

The python script angr_t2.py performs symbolic execution on binary angr2 and stores the output to print easter egg to input1_t2 file.

Following are the steps used

1. First load our binary into angr, initializa the state and create a simulation manager

2. Use gdb or ghidra to check the function that we need to write SimProcedure for.

	While analyzing the binary in ghidra, we notice function mm() in check()
	
	cVar1 = mm();
	cVar1 is of type character, while mm() returns integer

	__snprintf_chk(acStack_78,100,1,0x65,"bash -c \'exit $(( %d + 4))\'",(int)param_1);
	iVar1 = system(acStack_78);
	return iVar1 >> 8;
	Further analysing the binary using gdb, I noticed that the function executes the "bash -c 'exit $(( inp[0] + 4))'" and returns exit code which is same as (ord(inp[0]) + 4) where inp[0] is the first character of input and which is the first and only argument of the function mm()


3. Write the SimProcedure where the run() function will return the (c + 4) where c is an argument to the function mm(). I have added some constraints to make the processing easier. Since the integer is typecasted to char, I have constrained the r such that (r >= 4) and (r < 256)

4. Set up the hook such that when function mm() is called, it actually executes the SimProcedure function that I have written. We can either get the address of the mm() function which is 0x0x4007a0 or simply mention 'mm' in the hook funtion call

5. Use explore function to step and continue until the required instruction is reached and executed by simulation manager

6. Get the concrete input formed from the constraints using posix.dumps

7. Store the input in the file input1_t2

8. Pass the required input to binary and the easter agg is printed out

Command : cat input1_t2 | ./angr2