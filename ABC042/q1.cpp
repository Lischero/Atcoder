#include <iostream>
#include <string>
#define factors 3
using namespace std;

int main() {
    int a, b, c;
    int five = 0;
    int seven = 0;
    cin >> a >> b >> c;
    int l[factors] = {a, b, c};
    for (int tmp = 0; tmp < factors; tmp++){
        if (l[tmp] == 5){
            five++;
        }
        if (l[tmp] == 7){
            seven++;
        }
    }
    if (five == 2 && seven == 1){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
