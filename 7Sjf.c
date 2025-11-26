#include <stdio.h>

int main() 
{
    int i = 0, j, n;
    int pno[10], bt[10], wt[10], tt[10];
    int temp = 0;
    float sum = 0, at = 0;

    printf("\nEnter the number of processes: ");
    scanf("%d", &n);

    printf("\nEnter the burst time of each process:\n");
    for (i = 0; i < n; i++) {
        pno[i] = i;  
        printf("p%d: ", i);
        scanf("%d", &bt[i]);
    }

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (bt[i] > bt[j]) {
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;

                temp = pno[i];
                pno[i] = pno[j];
                pno[j] = temp;
            }
        }
    }

    wt[0] = 0;
    for (i = 1; i < n; i++) {
        wt[i] = bt[i - 1] + wt[i - 1];
        sum += wt[i];
    }

    printf("\nProcess No\tBurst Time\tWaiting Time\tTurnaround Time\n");

    for (i = 0; i < n; i++) {
        tt[i] = bt[i] + wt[i];
        at += tt[i];
        printf("p%d\t\t%d\t\t%d\t\t%d\n", pno[i], bt[i], wt[i], tt[i]);
    }

    printf("\nAverage Waiting Time = %.2f", sum / n);
    printf("\nAverage Turnaround Time = %.2f\n", at / n);

    return 0;
}
