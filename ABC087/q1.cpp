#include <iostream>
#include <string>
using namespace std;

int main() {
    int x, a, b;
    cin >> x;
    cin >> a;
    cin >> b;
    x -= a;
    x -= ((int)(x/b))*b;
    cout << x << endl;
    return 0;
}
