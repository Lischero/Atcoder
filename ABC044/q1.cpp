#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, k, x, y;
    cin >> n;
    cin >> k;
    cin >> x;
    cin >> y;
    if (n >= k){
        cout << x*k + y*(n-k) << endl;
    } else {
        cout << x*n << endl;
    }
    return 0;
}
