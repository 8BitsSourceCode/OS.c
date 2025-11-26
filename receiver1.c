#include "mesg.h"

int main() {
    int mq_id;
    mesg msg;

    if ((mq_id = msgget(MKEY1, PERMS | IPC_CREAT)) < 0) {
        perror("Receiver: Error opening message");
        exit(1);
    }

    printf("Waiting for message...\n");
    if (msgrcv(mq_id, &msg, sizeof(msg.mdata), 1111L, 0) < 0) {
        perror("Receiver: Error receiving message");
        exit(1);
    }

    printf("Received message: %s\n", msg.mdata);
    msgctl(mq_id, IPC_RMID, NULL);
    return 0;
}
