#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    string a, b;
    cin >> a;
    cin >> b;
    if (a.length() > b.length()){
        cout << a << endl;
    } else {
        cout << b << endl;
    }
    return 0;
}
