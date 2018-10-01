#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int ans = 700;
    cin >> s;
    for (int tmp = 0; tmp < (int)s.size(); tmp++){
        if (s[tmp] == 'o'){
            ans += 100;
        }
    }
    cout << ans << endl;
    return 0;
}
