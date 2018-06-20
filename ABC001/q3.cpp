#include <iostream>
#include <string>
#include <map>
#include <cmath>
using namespace std;

int main() {
    double deg, dis;
    int degree, indexDirection, indexPower;
    
    map<int, string> windDirectionName = 
        {
            {0, "NNE"}, {1, "NE"}, {2, "ENE"}, {3, "E"}, 
            {4, "ESE"}, {5, "SE"}, {6, "SSE"}, {7, "S"},
            {8, "SSW"}, {9, "SW"}, {10, "WSW"}, {11, "W"},
            {12, "WNW"}, {13, "NW"}, {14, "NNW"}, {15, "N"}
        };
    map<int, int> windPower1 = 
        {
            {0, 14}, {1, 92}, {2, 200}, {3, 326}, {4, 476}, {5, 644}, {6, 830},
            {7, 1028}, {8, 1244}, {9, 1466}, {10, 1706}, {11, 1958}
        };
    map<int, int> windPower2 = 
        {
            {0, 0}, {1, 15}, {2, 93}, {3, 201}, {4, 327}, {5, 477}, {6, 645},
            {7, 831}, {8, 1029}, {9, 1245}, {10, 1467}, {11, 1707}, {12, 1959}
        };

    cin >> deg >> dis;
    for (degree = 113, indexDirection = 0; indexDirection <= 14; degree += 225, indexDirection++){
        if (degree <= deg && deg <= degree+224){
            break;
        }
    }

    for (indexPower = 0; indexPower <= 12; indexPower++){
        if (indexPower != 12){
            if (windPower2[indexPower] <= dis && dis <= windPower1[indexPower]){
                break;
            }
        } else {
            if (windPower2[indexPower] <= dis){
                break;
            }
        }
    }

    if (indexPower == 0){
        cout << "C " << indexPower << endl;
    } else {
        cout << windDirectionName[indexDirection] << " " << indexPower << endl;
    }

    return 0;
}
