#include <iostream>
#include <string>
#include <bitset>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    bool flags[n][n] = {};
    int ans = 0;
    for (int tmp = 0; tmp < m; tmp++){
        int x, y;
        cin >> x >> y;
        flags[--x][--y] = true;
        flags[y][x] = true;
    }
    for (int sample = (1 << n); --sample;){
        int bits = bitset<13>(sample).count();
        if (bits <= ans){
            continue;
        }
        for (int tmp = 0; tmp < n; tmp++){
            for (int tmp2 = tmp+1; tmp2 < n; tmp2++){
                if (sample&(1 << tmp) && sample&(1 << tmp2) && !flags[tmp][tmp2]){
                    goto firstloop;
                }
            }
        }
        ans = bits;
        firstloop:;
    }
    cout << ans << endl;
    return 0;
}
