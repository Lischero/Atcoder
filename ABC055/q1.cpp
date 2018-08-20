#include <iostream>
#include <string>
#define value 800
using namespace std;

int main() {
    int n, a;
    cin >> n;
    a = n/15;
    cout << value*n - 200*a << endl;
    return 0;
}
