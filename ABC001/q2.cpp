#include <iostream>
#include <string>
using namespace std;

int main(){
    double m;
    cin >> m;
    m /=1000;
    if (m < 0.1){
        cout << "00" << endl;
        return 0;
    } else if (m <= 5){
        m *= 10;
    } else if (m >= 6 && m <= 30){
        m += 50;
    } else if (m >= 35 && m <= 70){
        m = (m-30)/5 + 80;
    } else {
        m = 89;
    }

    if (m <= 9){
        cout << "0" << (int)m << endl;
    } else {
        cout << (int)m << endl;
    }
    return 0;
}
