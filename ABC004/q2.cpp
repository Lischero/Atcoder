#include <iostream>
#include <sstream>
#include <string>
#define X 4
#define Y 4
using namespace std;

int main() {
    string factors[Y][X];
    string buf;
    for (int y = 0; y < Y; y++){
        getline(cin, buf);
        stringstream ss(buf);
        for (int x = 0; getline(ss, buf, ' '); x++){
            factors[y][x] = buf;
        }
    }
    for (int y = Y-1; y >= 0; y--){
        for (int x = X-1; x >= 0; x--){
            if (x){
                cout << factors[y][x] << ' ';
            } else {
                cout << factors[y][x] << endl;
            }
        }
    }
    return 0;
}
