#include <stdio.h>

int isPrime(int factor){
    int a = 2;
    while (factor >= a*a){
        if (!(factor%a)){
            return 0;
        }
        a++;
    }
    return 1;
}

int main(void){
    int num = 0, ans = 0;
    scanf("%d", &num);
    for(int counter = 1; counter <= num; counter++){
        if (isPrime(counter) && counter%2 == 0){
            ans++;
        }
    }
    printf("%d\n", ans);
}
