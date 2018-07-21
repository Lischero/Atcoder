#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int a;
    cin >> a;
    int ans = -1;
    for (int tmp = 0; tmp < a+1; tmp++){
        ans = max(tmp*(a-tmp), ans);
    }
    cout << ans << endl;
    return 0;
}
