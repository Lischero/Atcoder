#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n, ans;
    cin >> n;
    ans = floor(n/2.0);
    if (n%2){
        cout << ans+1 << endl;
    } else {
        cout << ans << endl;
    }
    return 0;
}
