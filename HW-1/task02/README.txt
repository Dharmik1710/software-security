command: 
ln -s flag.txt tmp
./my_cat tmp

In my_cat.c file, the function checks if the filename passed as input parameter consists of the characters 'f', 'l', 'a' or 'g' in it. If the filename consists these characters, it will exit. 

We can create a symbolic link with filename 'tmp'(characters other than 'f','l','a','g') and point it to flag. This will bypass the first set of conditions. Real UID is task02 and Effective UID is task02flag. The binary will run as effective user ID and print the content from the falg.txt.
