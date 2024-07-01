Command: awk -v arg=$(( ($(date +%s) -20)*65539 + 4282663 )) 'BEGIN { system("./predict_rand "  arg) }' | head -n 1

Seed function called from main function sets the state(global variable) which is current time in seconds minus 20. Function get_rand is called which return [(state * a) + c]. The if condiction compares value returned by get_rand function and user value passed in parameter is equal. If its equal then it reads the flag. 

SetUID bit of predict_rand binary is set and the real user ID is task01 and effective user ID is task01flag which own the flag.txt file. Hence if we pass the expected value by calculating value beforehand(the task may take milliseconds if done inline command), then the if condition will always be true and flag will be read and printed to standard output.
