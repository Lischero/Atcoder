#include <stdio.h>
#define factor 51
int main(void){
	char sentence[factor] = {'\0'};
	int i;
	scanf("%s",sentence);
	for(i = 0; i < factor; i++){
		if(sentence[i]=='\0'){
			i--;
			break;
		}
	}
	if(sentence[i]=='T'){
		printf("YES\n");
	} else {
		printf("NO\n");
	}
	return 0;
}
