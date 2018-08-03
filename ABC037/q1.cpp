#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << int(c/min(a,b)) << endl;
    return 0;
}
