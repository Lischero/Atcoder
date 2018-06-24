#include <iostream>
#include <string>
using namespace std;

int main() {
    string w;
    cin >> w;
    for (int tmp = 0; tmp < int(w.length()); tmp++){
        if (w[tmp] != 'a' && w[tmp] != 'i' && w[tmp] != 'u' && w[tmp] != 'e' && w[tmp] != 'o'){
            cout << w[tmp];
        }
    }
    cout << endl;
    return 0;
}
