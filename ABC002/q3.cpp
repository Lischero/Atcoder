#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int x1, y1, x2, y2, x3, y3;
    double ans;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    x1 -= x3;
    x2 -= x3;
    y1 -= y3;
    y2 -= y3;
    ans = abs(x1*y2 - x2*y1)*0.5; 
    cout << fixed << setprecision(1) << ans << endl;
    return 0;
}
