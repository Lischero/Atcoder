#include <stdio.h>
int main (void){
	unsigned int a = 1, b = 1,ans;
	scanf("%d %d",&a,&b);
	ans = b/a;
	if(b%a){
		ans++;
	}
	printf("%d\n",ans);
	return 0;
}
