command : ./echo_as_a_service '\n"; cat flag.txt; echo "'

The echo function in echo_as_a_service uses an insecure implementation of echo command in linux.

It inserts the user input given as argument directly into the command buffer without santizing the input. We can pass a string that terminatesthe echo command using ';', add our command(cat flag.txt) and again initiate the echo command. The binary will run as effective user ID which is task03flag.
