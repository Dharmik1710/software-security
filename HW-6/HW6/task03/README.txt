For this task, I have used angr to create segmentation fault when the program is run with input as mentioned in input1_t3 file.

The python script angr_t3.py performs symbolic execution on binary angr1 and stores the output to cause segmentation fault in input1_t3 file.

Following are the steps used

1. First load our binary into angr, initializa the state and create a simulation manager. To keep the memory consumption low, I have discarded deadended paths by generating a SimulationManager using the auto_drop.

2. I have first stepped into function to create an active path into simulation manager

3. Use while loop or list comprehension to get to the state where we find our first unconstrained path.

4. Save the unconstrained state to ucstate

5. Print out rip register to confirm if the reached state is indeed an unconstrained state.

6. Get the concrete input using ucstate.posix.dumps()

5. Store the input in the file input1_t3

6. Pass the required input to binary and the program causes segmentation fault

