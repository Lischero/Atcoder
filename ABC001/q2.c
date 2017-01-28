#include <stdio.h>

int main (void){
    int m, tmp;
    double km;
    scanf("%d", &m);
    km = (double) m / 1000;
    if(km < 0.1){
        printf("00\n");
    } else if(km <= 5){
        tmp = (int) (km * 10);
        (tmp < 10) ? printf("0%d\n",tmp) : printf("%d\n",tmp);
    } else if(km >= 6 && km <= 30){
        tmp = (int) km + 50;
        printf("%d\n",tmp);
    } else if(km >= 35 && km <= 70){
        tmp = ( (int) km - 30 ) / 5 + 80;
        printf("%d\n",tmp);
    } else if(km > 70){
        printf("89\n");
    }
    return 0;
}
