#include <stdio.h>

int main (void){
	int n = 1,q = 1,l = 0,r = 0,t = 0;
	scanf("%d %d", &n,&q);
	int a[100] = {0};
	while(q){
		scanf("%d %d %d",&l,&r,&t);
		l = l - 1;
		r = r - 1;
		while(l <= r){
			a[l] = t;
			l++;
		}
		q -= 1;
	}
	int c = 0;
	while(n-1 >= c){
		printf("%d\n",a[c]);
		c++;
	}
	return 0;
}
