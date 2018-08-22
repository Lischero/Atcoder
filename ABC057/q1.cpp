#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a+b >= 24){
        cout << a+b-24 << endl;
    } else {
        cout << a+b << endl;
    }
    return 0;
}
