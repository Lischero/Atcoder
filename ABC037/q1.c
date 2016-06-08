#include <stdio.h>

int main (void) {
	int a = 0,b = 0,c = 0,t = 0, i = 0,result = 0;
	scanf("%d %d %d",&a,&b,&c);
	while(c > 0){
		t = c/a;
		i = c/b;
		if(t >= i){
			c -= t*a;
			result += t;
		} else {
			c -= i*b;
			result += i;
		}
		if(c < b | c < a) break;
	}
	printf("%d\n",result);
	return 0;
}
