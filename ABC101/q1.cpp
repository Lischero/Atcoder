#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int ans = 0;
    cin >> s;
    for (int tmp = 0; tmp < (int)s.size(); tmp++){
        if (s[tmp] =='+'){
            ans += 1;
        } else {
            ans -= 1;
        }
    }
    cout << ans << endl;
    return 0;
}
