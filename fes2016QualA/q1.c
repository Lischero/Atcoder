#include <stdio.h>

int main(void){
	char s[14] = {'\0'};
	scanf("%s",s);
	for(int a = 13; a >= 0; a--){
		s[a] = s[a-1];
		if(a == 4){
			s[a] = ' ';
			break;
		}
	}
	printf("%s\n",s);
	return 0;
}
