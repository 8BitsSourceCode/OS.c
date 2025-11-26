#include <stdio.h>
#include <stdlib.h>

int mutex = 1, wrt = 1, readcount = 0;

int wait(int s) { return (--s); }
int signal(int s) { return (++s); }

void reader() {
    mutex = wait(mutex);
    readcount++;
    if (readcount == 1)
        wrt = wait(wrt);
    mutex = signal(mutex);

    printf("\nReader is reading...");

    mutex = wait(mutex);
    readcount--;
    if (readcount == 0)
        wrt = signal(wrt);
    mutex = signal(mutex);
}

void writer() {
    wrt = wait(wrt);
    printf("\nWriter is writing...");
    wrt = signal(wrt);
}

int main() {
    int n;
    printf("\n1. Reader\n2. Writer\n3. Exit");
    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &n);
        switch (n) {
            case 1: if (mutex == 1) reader(); else printf("\nBusy!"); break;
            case 2: if ((wrt == 1) && (mutex == 1)) writer(); else printf("\nBusy!"); break;
            case 3: exit(0);
        }
    }
}
