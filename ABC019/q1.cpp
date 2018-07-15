#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> d = {a, b, c};
    sort(d.begin(), d.end());
    cout << d[1] << endl;
    return 0;
}
