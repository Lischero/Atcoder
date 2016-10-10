#include <stdio.h>
int main (void){
    long long int N, A, B, counter = 0;
    scanf("%lld %lld %lld",&N,&A,&B);
    char s[N+1];
    scanf("%s",s);
    long long int pass = 0;
    for(long long int i = 0; i < N; i++){
        if(s[i] == 'a' && pass < A+B){
            pass++;
            printf("Yes\n");
        } else if(s[i] == 'b' && pass < A+B && ++counter <= B){
            pass++;
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    return 0;
}
