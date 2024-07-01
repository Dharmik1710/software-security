Command:
python script.py

This program is vulnerable to buffer overflow. The program asks for user input and is stored in the 'user' object. The 'user[100]', i.e after 100 bytes it also stores the name of the function that is to be run. We need that memory space to store flag function reference instead of cat. 

Hence we design our user input string in such a way that it overwrites the memory from where the function decides to run either cat or flag function. The reference to the flag function can be obtained by looking at the assembly code.
