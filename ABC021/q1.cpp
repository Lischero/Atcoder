#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, factor, mod;
    cin >> n;
    factor = n/2;
    mod = n%2;
    cout << mod+factor << endl;
    if (mod){
        cout << mod << endl;
    }
    for (; factor != 0; factor--){
        cout << '2' << endl;
    }
    return 0;
}
