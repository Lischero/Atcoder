#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int a, b;
    cin >> a;
    cin >> b;
    if (a%b){
        cout << b - a%b << endl;
    } else {
        cout << '0' << endl;
    }
    return 0;
}
