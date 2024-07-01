#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

int main(void) {
    int iVar1;
    DIR *__dirp;
    char *__s;
    size_t sVar2;
    struct dirent *__pdVar3;

    // Open the "/home/" directory
    __dirp = opendir("/home/");
    if (__dirp == (DIR *)0x0) {
        perror("Couldn't open the directory");
        exit(1);
    }

    do {
        // Read the next entry in the directory
        __pdVar3 = readdir(__dirp);

        // Check if we have reached the end of the directory
        if (__pdVar3 == (struct dirent *)0x0) {
            // Close the directory and return
            iVar1 = closedir(__dirp);
            return iVar1;
        }

        __s = __pdVar3->d_name;
        sVar2 = strlen(__s);

    } while ((sVar2 < 3) || (((*__s == 't' && (__s[1] == 'a')) && (__s[2] == 's')) && (__s[3] == 'k')));

    // Close the directory
    closedir(__dirp);

    // Print the product of the ASCII values of the first and third characters
    printf("%u\n", (unsigned int)(*__s) * (unsigned int)__s[2]);

    // Return the same value
    return (unsigned int)(*__s) * (unsigned int)__s[2];
}

