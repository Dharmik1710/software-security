Supplemental file: scan_script

We can see that in the get_rnd_str function, a file named 'safepassword_{pid}' is created in order to store the random bytes generated from /dev/urandom. The file is deleted once the random_string which is generated is copied to the buffer.

The code compares the generated password(random string) and the user entered password. If the match is successful, it reads and prints the flag. 

We can write a bash script(scan_script) that will continously check the '/tmp' directory for file 'safepassword_*' using regex. If the file is found we canprint out the file content, which is the password.

We enter the password into the promp 'admin password', and the flag is printed out.
