#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    double rate1 = 0;
    double rate2 = 0;
    string buf;
    vector<int> data;

    cin >> n >> k;
    cin.ignore();
    getline(cin, buf);
    stringstream ss(buf);
    while(getline(ss, buf, ' ')){
        data.push_back(atoi(buf.c_str()));
    }
    sort(data.begin(), data.end());

    for (int tmp = n-k; tmp < n; tmp++){
        rate1 = (rate1+data[tmp])/2;
    }
    for (int tmp = n-1; n-k <= tmp; tmp--){
        rate2 = (rate2+data[tmp])/2;
    }
    cout << fixed << setprecision(3) << max(rate1, rate2) << endl;
    return 0;
}
