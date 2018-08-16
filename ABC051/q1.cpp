#include <iostream>
#include <string>
#define num 19
using namespace std;

int main() {
    string s;
    cin >> s;
    for (int tmp = 0; tmp < num; tmp++){
        if (s[tmp] == ','){
            s[tmp] = ' ';
        }
    }
    cout << s << endl;
    return 0;
}
