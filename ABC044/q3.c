#include <stdio.h>

typedef unsigned long long ull;

int main(void){
	int N, A, max = -1;
	int x[51] = {0};
	scanf("%d %d",&N,&A);
	for(int a = 1; a < N+1; a++) scanf("%d", &x[a]);
	for(int a = 1; a < N+1; a++){
		if(x[a] > max) max = x[a];
	}
	if(max < A) max = A;

	ull list[N+1][N+1][N*max+1];
	ull result = 0;

	for(int a = 0; a < N+1; a++){
		for(int b = 0; b < N+1; b++){
			for (int c = 0; c < N*max+1; c++){
				if(!a && !b && !c){
					list[a][b][c] = 1; //first principle
				} else if(a >= 1 && c < x[a]){
					list[a][b][c] = list[a-1][b][c]; // second principle
				} else if(a >= 1 && b >= 1 && c >= x[a]){
					list[a][b][c] = list[a-1][b][c] + list[a-1][b-1][c-x[a]]; // third principle
				} else {
					list[a][b][c] = 0; // fourth principle
				}
			}
		}
	}

	for(int a = 1; a < N+1; a++) result += list[N][a][a*A];
	printf("%llu\n",result);
	return 0;
}

