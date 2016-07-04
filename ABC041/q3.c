#include <stdio.h>
#include <stdlib.h>

typedef struct{
	unsigned long long int height;
	unsigned long int number;
}student;

int comp(const void *a, const void *b){
	student test1 = *(student *)a;
	student test2 = *(student *)b;
	int tmp1 = test1.height;
	int tmp2 = test2.height;
	return tmp2 - tmp1;
}

int main (void){
	unsigned long int N;
	scanf("%ld", &N);
	student a[N];
	for(unsigned long int count = 0; count < N; count++){
		scanf("%lld",&a[count].height);
		a[count].number = count + 1;
	}
	qsort(a, N, sizeof(student), comp);
	for(unsigned long int count = 0; count < N; count++){
		printf("%ld\n",a[count].number);
	}
	return 0;
}	
