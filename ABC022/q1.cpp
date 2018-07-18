#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n, s, t, w;
    int ans = 0;
    cin >> n >> s >> t;
    cin >> w;
    for (int tmp = 0; tmp < n; tmp++){
        if (s <= w && w <= t){
            ans++;
        }
        if (tmp != n-1){
            int num;
            cin >> num;
            w += num;
        } else {
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
