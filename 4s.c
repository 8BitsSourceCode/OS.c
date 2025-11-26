#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <stdlib.h>

int main() {
    int fd1, fd2;
    char buf1[50] = "just a test\n";
    char buf2[100];

    fd1 = open("file1", O_RDWR | O_CREAT | O_TRUNC, 0644);
    fd2 = open("file2", O_RDWR | O_CREAT | O_TRUNC, 0644);

    if (fd1 < 0 || fd2 < 0) {
        perror("File open error");
        return 1;
    }

    write(fd1, buf1, strlen(buf1));

    printf("\nEnter the text now: ");
    fgets(buf1, sizeof(buf1), stdin);

    write(fd1, buf1, strlen(buf1));

    lseek(fd1, 0, SEEK_SET);

  
    int n = read(fd1, buf2, sizeof(buf2));
    buf2[n] = '\0';

  
    write(fd2, buf2, strlen(buf2));

    close(fd1);
    close(fd2);

    printf("\nDone.\n");
    return 0;
}

