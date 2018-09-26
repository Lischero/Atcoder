#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char s[3][3];
    for (int tmp = 0; tmp < 3; tmp++){
        cin >> s[tmp];
    }
    cout << s[0][0] << s[1][1] << s[2][2] << endl;
    return 0;
}
