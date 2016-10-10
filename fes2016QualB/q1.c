#include <stdio.h>
int main (void){
    char t[17] = "CODEFESTIVAL2016";
    char s[17] = {'\0'};
    int ans = 0;
    scanf("%s",s);
    for(int i = 0; i < 17; i++){
        if(t[i] == s[i]){
            continue;
        } else {
            ans++;
        }   
    }
    printf("%d\n",ans);
    return 0;
}
