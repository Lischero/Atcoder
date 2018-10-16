#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << max(a*10+b+c, max(a+b*10+c, a+b+c*10)) << endl;
    return 0;
}
