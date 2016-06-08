#include <stdio.h>
#define factor 100000
unsigned long int result = 0;
unsigned long int N;
unsigned long int numbers[factor] = {0};
void check(unsigned long int l, unsigned long int r){
	for(unsigned long int p = 1; p <= r - l; p++){
		result += p;
	}
}
int main(void){
	unsigned long int l,r;
	scanf("%ld",&N);
	result += N;
	for(l = 0; l < N; l++) scanf("%ld",&numbers[l]);
	for(l = 0; l < N; l++){
		r = l;
		if(l < N-1 && numbers[l] < numbers[l+1]){ //l == rの(l,r)はresultに足し済みのため。
			while( r < N-1 && numbers[r] < numbers[r+1]) r++;
			check(l,r);
		}
		l = r;
	}
	printf("%ld\n",result);
	return 0;
}	
