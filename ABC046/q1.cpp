#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> l = {a, b, c};
    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    cout << l.size() << endl;
    return 0;
}
