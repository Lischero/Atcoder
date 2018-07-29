#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, n;
    cin >> a;
    cin >> b;
    cin >> n;
    for (int tmp = n; ;tmp++){
        if (tmp%a == 0 && tmp%b == 0){
            cout << tmp << endl;
            break;
        }
    }
    return 0;
}
