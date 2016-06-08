#include <stdio.h>
#include <stdlib.h>
int main (void){
	int n, k, c, t;
	unsigned long int answer = 0;
	scanf("%d %d",&n,&k);
	int *a;
	a = (int *)malloc(sizeof(int)*n);
	for(c = 0; c < n; c++){
		scanf("%d",&a[c]);
	}

	for(c = 0; c < (n-k+1); c++){
		for(t = c; t< c+k; t++){
			answer += a[t];
		}
	}
	printf("%ld\n",answer);
	return 0;
}
