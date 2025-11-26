#include <stdio.h>

struct process {
    int burst, wait, comp, remaining;
} p[20];

int main() {
    int n, quantum, i, time = 0, done, totalwait = 0, totalturn = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter quantum time: ");
    scanf("%d", &quantum);

    for (i = 0; i < n; i++) {
        printf("Enter burst time for Process %d: ", i + 1);
        scanf("%d", &p[i].burst);
        p[i].remaining = p[i].burst;
        p[i].wait = 0;
        p[i].comp = 0;
    }

    printf("\nExecution Order:");
    printf("\nProcess\tStart\tEnd\tRemaining");

    do {
        done = 1;

        for (i = 0; i < n; i++) {

            if (p[i].remaining > 0) {

                done = 0;

                int start = time;

                if (p[i].remaining > quantum) {
                    time += quantum;
                    p[i].remaining -= quantum;
                } else {
                    time += p[i].remaining;
                    p[i].comp = time;
                    p[i].remaining = 0;
                }

                printf("\nP%-7d%-7d%-7d%-7d", i + 1, start, time, p[i].remaining);
            }
        }

    } while (!done);

    printf("\n\nProcess\tWaiting Time\tTurnaround Time");

    for (i = 0; i < n; i++) {
        p[i].wait = p[i].comp - p[i].burst;
        int tat = p[i].burst + p[i].wait;

        printf("\nP%-7d%-15d%-15d", i + 1, p[i].wait, tat);

        totalwait += p[i].wait;
        totalturn += tat;
    }

    printf("\n\nAverage Waiting Time: %.2f", totalwait / (float)n);
    printf("\nAverage Turnaround Time: %.2f\n", totalturn / (float)n);

    return 0;
}
