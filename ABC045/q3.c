#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char s[11] = {'\0'};

void split(char *ptr, char* ptr2, int factor, int length){ /*ptrはコピー先、ptr2は切り取りコピーの素配列、factorは開始位置、lengthは切り出し個数。*/
	int num = 0;
	for(int a = factor; a < factor+length; a++) ptr[num++] = ptr2[a];
}

long long int add(char *ptr){
	long long int ans = atoll(ptr);
	int size = strlen(ptr);
	for(int a = 1; a < size; a++){
		char tmp[11] = {'\0'};
		char tmp2[11] = {'\0'};
		split(tmp,ptr,0,a);
		ans += atoll(tmp)*powl(2,size - a - 1);
		split(tmp2,ptr,a,size-a);
		ans += add(tmp2);
	}
	return ans;
}

int main(void){
	long long int result = 0; /*factorは配列の長さとする。*/
	scanf("%s",s);
	result = add(s);
	printf("%lld\n",result);
	return 0;
}	
