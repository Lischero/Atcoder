#include <stdio.h>
int main (void){
    int K, T;
    int a[100] = {0};
    int maxfactor, sum = 0, max = -1;
    scanf("%d %d", &K, &T);
    for(int i = 0; i < T; i++) scanf("%d", &a[i]);
    for(int i = 0; i < T; i++){
        if(max < a[i]){
            max = a[i];
            maxfactor = i;
        }
    }
    /*int pair = (max+1)/2;
    int counter = 0;
    for(int i = 0; i < T; i++){
        if(i != maxfactor){
            while(counter/2 == pair){
                if(a[i] <= 0) break;
                a[i]--;
                counter++;
            }
        }
    }
    if(counter/2 == pair){
        printf("0\n");
    }*/

    for(int i = 0; i < T; i++){
        if(i != maxfactor){
            sum += a[i];
        }
    }
    if(sum+1 < a[maxfactor]){
        printf("%d\n",a[maxfactor]-sum-1);
    } else {
        printf("0\n");
    }
    return 0;
}





    

