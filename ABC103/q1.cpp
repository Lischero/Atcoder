#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int ans = 0;
    vector<int> a(3, 0);
    for (int tmp = 0; tmp < (int)a.size(); tmp++){
        int b;
        cin >> b;
        a[tmp] = b;;
    }
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());
    for (int tmp = 0; tmp < (int)a.size()-1; tmp++){
        ans += abs(a[tmp] - a[tmp+1]);
    }
    cout << ans << endl;
    return 0;
}
