#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    double ans = 0;
    for (double tmp = 10000; tmp <= 10000*n; tmp += 10000){
        ans += tmp;
    }
    ans /= n;
    cout << ans << endl;
    return 0;
}
