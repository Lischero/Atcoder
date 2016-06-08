#include <stdio.h>
#define MOD ((unsigned long int) 1e9+7)

//グローバル変数。
unsigned long int a[1000][1000];
unsigned long int stock[1000][1000]; //各経路上での合計の余り。
unsigned int h = 1,w = 1;

int search(int j, int i){
	unsigned long int result = 1;
	if(stock[j][i] > 0) return stock[j][i];
	if(0 <= (i-1) && a[j][i] < a[j][i-1]){
		result += search(j,i-1);
	}
	if((i+1) < w && a[j][i] < a[j][i+1]){
		result += search(j,i+1);
	}
	if(0 <= j-1 && a[j][i] < a[j-1][i]){
		result += search(j-1,i);
	}
	if((j+1) < h && a[j][i] < a[j+1][i]){
		result += search(j+1,i);
	}
	stock[j][i] = result % MOD;
	return stock[j][i];
}	

int main (void){
	unsigned long int result = 0;
	int i,j;
	for(j = 0; j < 1000; j++){
		for(i = 0; i < 1000; i++){
			a[j][i] = 0;
			stock[j][i] = 0;
		}
	}
	scanf("%d %d",&h,&w);
	for(j = 0; j < h; j++){
		for(i = 0; i < w; i++){
			scanf("%ld",&a[j][i]);
		}
	}

	for(j = 0; j < h; j++){
		for(i = 0; i < w; i++){
			search(j,i);
		}
	}

	for(j = 0; j < h; j++){
		for(i = 0; i < w; i++){
			result += stock[j][i];
			result %= MOD;
		}
	}
	printf("%ld\n",result);
	return 0;
}
