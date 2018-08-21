#include <iostream>
#include <string>
using namespace std;

int main() {
    char a, b;
    cin >> a >> b;
    if (a == 'H'){
        if (b == 'H'){
            cout << "H" << endl;
            return 0;
        }
    } else {
        if (b == 'D'){
            cout << "H" << endl;
            return 0;
        }
    }
    cout << "D" << endl;
    return 0;
}
