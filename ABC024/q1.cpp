#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c, k, s, t;
    cin >> a >> b >> c >> k;
    cin >> s >> t;
    if (s+t >= k){
        cout << (a-c)*s+(b-c)*t << endl;
    } else {
        cout << a*s+b*t << endl;
    }
    return 0;
}
