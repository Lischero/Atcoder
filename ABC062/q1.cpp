#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    map<int, int> factors = 
    { {1,1}, {3,1}, {5,1}, {7,1}, {8,1}, {10,1}, {12,1},
      {4,2}, {6,2}, {9,2}, {11,2}, {2,3} };
    int x, y;
    cin >> x >> y;
    if (factors[x] == factors[y]){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
