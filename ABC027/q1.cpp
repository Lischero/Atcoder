#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> d = { a, b, c };
    if (a == b && b == c){
        cout << a << endl;
    } else {
        if (a == b){
            cout << c << endl;
        } else if(a == c){
            cout << b << endl;
        } else {
            cout << a << endl;
        }
    }
    return 0;
}
