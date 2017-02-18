#include <stdio.h>
int main(void){
    long long int N, M;
    scanf("%lld %lld", &N, &M);
    long long int ans = (N+M/2)/2;
    printf("%lld\n", ans);
    return 0;
}
