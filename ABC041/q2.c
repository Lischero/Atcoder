#include <stdio.h>
int main (void){
	unsigned long long int A, B, C, X;
	scanf("%lld %lld %lld",&A,&B,&C);
	X = (A * B) % 1000000007;
	X = (X * C) % 1000000007;
	printf("%lld\n",X);
	return 0;
}
