#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int n;
    int ans = 0;
    cin >> n;
    vector<int> a;
    map<int, int> b;
    for (int loop = 0, tmp = 0; loop < n; loop++){
        cin >> tmp;
        if (b[tmp]){
            b[tmp]++;
        } else {
            b[tmp] = 1;
            a.push_back(tmp);
        }
    }
    for (int loop = 0; loop < (int)a.size(); loop++){
        if (a[loop] > b[a[loop]]){
            ans += b[a[loop]];
        } else if(a[loop] < b[a[loop]]){
            ans += b[a[loop]]-a[loop];
        } else {
        }
    }
    cout << ans << endl;
    return 0;
}
