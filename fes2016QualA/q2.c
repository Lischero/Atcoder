#include <stdio.h>

int main (void){
	int N;
	scanf("%d",&N);
	int a[N];
	int result = 0;
	for(int i = 0; i < N; i++){
		scanf("%d",&a[i]);
	}
	for(int i = 0; i < N; i++){
		if(a[i] == i+1){
			continue;
		}
		int j = a[i] - 1;
		if(a[j] == i+1){
			a[i] = 0;
			a[j] = 0;
			result++;
		}
			
	}
	printf("%d\n",result);
	return 0;
}
