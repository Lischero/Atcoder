#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    map<char, int> l{ {'A',10}, {'B',11}, {'C',12}, {'D',13}, {'E',14}, {'F',15} };
    char x, y;
    cin >> x >> y;
    if (l[x] < l[y]){
        cout << "<" << endl;
    } else if (l[x] == l[y]){
        cout << "=" << endl;
    } else {
        cout << ">" << endl;
    }
    return 0;
}
