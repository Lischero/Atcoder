#include <stdio.h>

char sa[101] = {'\0'};
char sb[101] = {'\0'};
char sc[101] = {'\0'};
int a = 0,b = 0,c = 0;

int check(char *ptr,int i){
	int checker;
	checker = *(ptr+i) - '\0';	
	return checker;
}

int check2(char *ptr, int i){
	if(*(ptr+i) == 'a'){
		return 1;
	} else if(*(ptr+i) == 'b'){
		return 2;
	} else {
		return 3;
	}
}

int search(int n){
	int tmp, result, s;
	char *ptr;
	while(1){
		result = n;
		if(n == 1){
			ptr = sa;
			tmp = check(ptr,a);
			s = a;
			a++;
		} else if(n == 2){
			ptr = sb;
			tmp = check(ptr,b);
			s = b;
			b++;
		} else { 
			ptr = sc;
			tmp = check(ptr,c);
			s = c;
			c++;
		}
		if(!tmp){
			break;
		}
		n = check2(ptr,s);
	}
	return result;
}
	
int main(void){
	int ans;
	scanf("%s",sa);
	scanf("%s",sb);
	scanf("%s",sc);
	ans = search(1);
	if(ans == 1){
		printf("A\n");
	} else if(ans == 2){
		printf("B\n");
	} else {
		printf("C\n");
	}
	return 0;
}
