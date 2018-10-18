#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    if (n == 1){
        cout << "Hello World" << endl;
    } else if(n == 2){
        cin >> a;
        cin >> b;
        cout << a+b << endl;
    }   
    return 0;
}
