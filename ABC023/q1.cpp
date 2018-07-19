#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    string x;
    int ans = 0;
    cin >> x;
    for (int tmp = 0; tmp < x.length(); tmp++){
        ans += x[tmp] - '0';
    }
    cout << ans << endl;
    return 0;
}
