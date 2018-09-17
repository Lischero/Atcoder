#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if ((a+b)%2){
        cout << (int)((a+b)/2.0)+1 << endl;
    } else {
        cout << (a+b)/2 << endl;
    }
    return 0;
}
