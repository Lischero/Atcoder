#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    cout << min(a,b)+min(c, d) << endl;
    return 0;
}
