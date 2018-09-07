#include <iostream>
#include <string>
using namespace std;

int main() {
    int x, t;
    cin >> x >> t;
    if (x >= t){
        cout << x-t << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}
