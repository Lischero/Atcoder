#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    string s, t;
    cin >> s;
    cin >> t;
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    reverse(t.begin(), t.end());
    if (s < t){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
