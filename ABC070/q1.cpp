#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;
    if (n[0] != n[2]){
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }
    return 0;
}
