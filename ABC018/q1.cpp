#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    vector<int> v;
    vector<int> v2;
    int num;
    for (int tmp = 0; tmp < 3; tmp++){
        cin >> num;
        v.push_back(num);
        v2.push_back(num);
    }
    sort(v.begin(), v.end(), greater<int>());
    for (int index2 = 0; index2 < 3; index2++){
        for (int index = 0; index < 3; index++){
            if (v2[index2] == v[index]){
                cout << index+1 << endl;
                break;
            }
        }
    }
    return 0;
}
