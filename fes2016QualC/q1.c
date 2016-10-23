#include <stdio.h>
int main (void){
    char s[101] = {"\0"};
    scanf("%s",s);
    for(int i = 0; i < 100; i++){
        if(s[i] == 'C' || s[i] == 'F'){
            continue;
        } else {
            for(int j = i; j < 100; j++){
                if(s[j] == 'C' || s[j] == 'F'){
                    i = j - 1;
                    break;
                }
                s[j] = '\0';
            }
        }
    }
    for(int i = 0; i < 101; i++){
        if(s[i] == 'C'){
            for(int j = i+1; j < 101; j++){
                if(s[j] == 'F'){
                    printf("Yes\n");
                    return 0;
                }
            }
        }
    }
    printf("No\n");
    return 0;
}
