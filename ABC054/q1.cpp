#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, c, d;
    int l[13] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1};
    cin >> a >> b;
    for (int tmp = 0; tmp < 2; tmp++){
        for (int tmp2 = 0; tmp2 < 13; tmp2++){
            if (l[tmp2] == a){
                c = tmp2;
            }
            if (l[tmp2] == b){
                d = tmp2;
            }
        }
    }
    if (c < d){
        cout << "Bob" << endl;
    } else if(a == b){
        cout << "Draw" << endl;
    } else {
        cout << "Alice" << endl;
    }
    return 0;
}
