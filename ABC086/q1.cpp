#include <iostream>
#include <string>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    if ((a*b)%2){
        cout << "Odd" << endl;
    } else {
        cout << "Even" << endl;
    }
    return 0;
}
