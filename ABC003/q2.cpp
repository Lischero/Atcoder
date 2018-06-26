#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s, t;
    int flag = 0;
    cin >> s;
    cin >> t;
    for (int tmp = 0; tmp < s.length(); tmp++){
        if (s[tmp] != t[tmp]){
            if (s[tmp] == '@' && (t[tmp] == 'a' || t[tmp] == 't' || t[tmp] == 'c' || t[tmp] == 'o' || t[tmp] == 'd' || t[tmp] == 'e' || t[tmp] == 'r')){
                continue;
            }
            if (t[tmp] == '@' && (s[tmp] == 'a' || s[tmp] == 't' || s[tmp] == 'c' || s[tmp] == 'o' || s[tmp] == 'd' || s[tmp] == 'e' || s[tmp] == 'r')){
                continue;
            }
            flag = 1;
            break;
        }
    }
    if (flag){
        cout << "You will lose" << endl;
    } else {
        cout << "You can win" << endl;
    }
    return 0;
}
