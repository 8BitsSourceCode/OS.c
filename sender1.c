#include "mesg.h"

int main() {
    int mq_id;
    int n;
    mesg msg;

    if ((mq_id = msgget(MKEY1, PERMS | IPC_CREAT)) < 0) {
        perror("Sender: Error creating message");
        exit(1);
    }

    msg.mtype = 1111L;
    printf("Enter message to send: ");
    fflush(stdout);

    n = read(0, msg.mdata, sizeof(msg.mdata) - 1);
    msg.mdata[n] = '\0';

    if (msgsnd(mq_id, &msg, sizeof(msg.mdata), 0) < 0) {
        perror("Sender: Error sending message");
        exit(1);
    }

    printf("Message sent successfully!\n");
    return 0;
}
