#include <iostream>
#include <string>
using namespace std;

int main(){
    int n, a;
    cin >> n;
    cin >> a;
    n -= ((int)(n/500))*500;
    if (n <= a){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
