#include <iostream>
#include <string>
using namespace std;

int main() {
    int w, h;
    cin >> w >> h;
    if (h*4 == 3*w || h*3 == w*4){
        cout << "4:3" << endl;
    } else if (h*16 == w*9 || h*9 == w*16){
        cout << "16:9" << endl;
    } else {
    }
    return 0;
}
