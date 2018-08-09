#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    int ans = 0;
    cin >> n;
    for (int tmp = 1; tmp <= n; tmp++){
        ans += tmp;
    }
    cout << ans << endl;
    return 0;
}
