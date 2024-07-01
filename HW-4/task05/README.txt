This is again the example of arbitrary read from and write to the memory and heap exploitation. 

We can notice there are four functions, two mallocs and two gets function. The mallocs assign 0x40 bytes in the heap. We can notice using gdb that the allocation in heap is continous. The one variable in the heap points to printf function while the another points to puts function. The offset between the two mallocs is 56 bytes.

The gets function gets the user input and calls the printf function without formatted string. We can exploit this to leak the address of the printf variable in stack and calculate the offset of that from the system call in libc. 

We can use the next puts function to overflow the buffer and overwrite the address of the printf function in the heap and overwrite it with the system address and the param which is (*printf + 1) is followed and give "/bin/sh".

Next instruction calls the printf function with params. 

My exploit will be 'a'*56, followed by the address of system call and followed by the '/bin/sh' string