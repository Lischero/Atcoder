#include <stdio.h>
int main(){
	int a;
	scanf("%d",&a);
	if(a<=59){
		puts("Bad");
	} else if(60<=a && 89>=a){
		puts("Good");
	} else if(90<=a && 99>=a){
		puts("Great");
	} else if(a==100){
		puts("Perfect");
	}
	return 0;
}
