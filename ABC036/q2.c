#include <stdio.h>
#include <stdint.h>
#define factor 50
int main (void){
	int n,x,y;
	char s[factor][factor];
	for(n = 0; n < factor; n++){
		s[n][n] = '\0';
	}
	scanf("%d",&n);
	for(y = 0; y < n; y++){
		scanf("%s",&s[y]);
	}
	for(x = 0; x < n; x++){
		for(y = n-1; y >= 0; y--){
			printf("%c",s[y][x]);
		}
		printf("\n");
	}
	return 0;
}		
