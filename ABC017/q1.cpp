#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    double s1, s2, s3, e1, e2, e3;
    cin >> s1 >> e1;
    cin >> s2 >> e2;
    cin >> s3 >> e3;
    int ans = s1*(e1/10.0)+s2*(e2/10.0)+s3*(e3/10.0);
    cout << ans << endl;
    return 0;
}
