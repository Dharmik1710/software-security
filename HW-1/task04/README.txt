command: 
awk -v arg="$(printf ';x%.0s' {1..50})" 'BEGIN { system("./secure_echo \"" arg "\"" ) }'


As we can notice from the code that instead of overwriting all the bytes, it replaces 2 bytes less as seen in the for loop condition. We have got a two byte window to write our exploit. One byte is occupied by ';', hence we are left with one more. We can write a bash script named with one letter(in my case 'x'), give the execution permissions(using chmod +x x) and include 'x' as one byte. The script can contains 'cat flag.txt'. 

Hence when system call is called on buffer, echo statement is called and then there are some space(bytes) and lastly a ';x'. Semicolon acts as a seperator for bash commands, and x is executed as effective UID.
