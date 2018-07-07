#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n >= 12){
        cout << '1' << endl;
    } else {
        cout << n+1 << endl;
    }
    return 0;
}
