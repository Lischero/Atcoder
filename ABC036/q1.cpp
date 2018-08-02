#include <iostream>
#include <string>
using namespace std;

int main() {
    double a, b;
    int ans;
    cin >> a >> b;
    if (a < b){
        if(int(b)%int(a) > 0){
            ans = int(b/a)+1;
        } else {
            ans = int(b/a);
        }
    } else {
        ans = 1;
    }
    cout << ans << endl;
    return 0;
}
