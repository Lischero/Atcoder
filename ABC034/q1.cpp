#include <iostream>
#include <string>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;
    if (x < y){
        cout << "Better" << endl;
    } else {
        cout << "Worse" << endl;
    }
    return 0;
}
