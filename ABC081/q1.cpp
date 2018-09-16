#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int count = 0;
    cin >> s;
    for (int tmp = 0; tmp < (int)s.size();){
        if (s[tmp++] == '1'){
            count += 1;
        }
    }
    cout << count << endl;
    return 0;
}
