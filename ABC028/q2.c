#include <stdio.h>
int main(){
	char s[101];
	char text='A';
	int a=0,b=0,c=0,d=0,e=0,f=0;
	scanf("%s",s);
	for(int i=0;i<101;i++){
		if(s[i]==text){
			a++;
		} else if(s[i]==text+1){
			b++;
		} else if(s[i]==text+2){
			c++;
		} else if(s[i]==text+3){
			d++;
		} else if(s[i]==text+4){
			e++;
		} else if(s[i]==text+5){
			f++;
		} else if(s[i]=='\0') {
			break;
		}
	}
	printf("%d %d %d %d %d %d\n",a,b,c,d,e,f);
	return 0;
}		
