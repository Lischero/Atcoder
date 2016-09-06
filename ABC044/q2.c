#include <stdio.h>
int main(void){
	char w[100] = {"\0"};
	scanf("%s",w);
	int number[26] = {0};
	for(int a = 0; a < 100; a++){
		if(!w[a]){
			break;
		}
		int difference = w[a] - 'a';
		number[difference] += 1;
	}
	for(int b = 0; b < 26; b++){
		if(number[b]%2 != 0){
			printf("No\n");
			return 0;
		}
	}
	printf("Yes\n");
	return 0;
}

