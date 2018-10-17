#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;
    for (int tmp = 0; tmp < (int)n.size(); tmp++){
        if (n[tmp] == '1'){
            n[tmp] = '9';
        } else if (n[tmp] =='9'){
            n[tmp] = '1';
        }
    }
    cout << n << endl;
    return 0;
}
