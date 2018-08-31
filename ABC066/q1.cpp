#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c, ans;
    cin >> a >> b >> c;
    ans = min(min(a+b, a+c), b+c);
    cout << ans << endl;
    return 0;
}
