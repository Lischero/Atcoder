#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int a, d;
    cin >> a >> d;
    cout << max((a+1)*d, a*(d+1)) << endl;
    return 0;
}
