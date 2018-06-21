#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main (){
    int n;
    vector<int> times(60/5*24+2, 0);
    vector<string> factors;
    cin >> n;
    for (int tmp = 0; tmp < n; tmp++){
        string a;
        while (getline(cin, a, '-')){
        cout << a  << endl;
            factors.push_back(a);
        }
    }
    for (int tmp = 0; tmp < factors.size(); tmp++){
            int hour = atoi(factors[tmp].substr(0,2).c_str());
            int minute = atoi(factors[tmp].substr(3).c_str());
            if (tmp%2){
                //fin
                minute += 5 - minute%5;
                times[hour*12+minute/5+1] -= 1;
            } else {
                //start
                minute -= minute%5;
                times[hour*12+minute/5] += 1;
            }
    }
    for (int tmp = 1; tmp < times.size(); tmp++){
        times[tmp] += times[tmp-1];
    }
    for (int tmp = 0, start_index = -1; tmp < times.size(); tmp++){
        if (times[tmp] != 0 && start_index == -1){
            start_index = tmp;
        }
        if (times[tmp] == 0 && start_index != -1){
            string start_time, end_time;
            int m_start_index = start_index%12;
            int h_start_index = (start_index-m_start_index)/12;
            int m_end_index = (tmp-1)%12;
            int h_end_index = (tmp-1-m_end_index)/12;
            m_start_index *= 5;
            m_end_index *= 5;

            if (h_start_index < 10){
                if (m_start_index < 10){
                    start_time = "0"+to_string(h_start_index)+"0"+to_string(m_start_index);
                } else{
                    start_time = "0"+to_string(h_start_index)+to_string(m_start_index);
                }
            } else {
                if (m_start_index < 10){
                    start_time = to_string(h_start_index)+"0"+to_string(m_start_index);
                } else{
                    start_time = to_string(h_start_index)+to_string(m_start_index);
                }
            }

            if (h_end_index < 10){
                if (m_end_index < 10){
                    end_time = "0"+to_string(h_end_index)+"0"+to_string(m_end_index);
                } else{
                    end_time = "0"+to_string(h_end_index)+to_string(m_end_index);
                }
            } else {
                if (m_end_index < 10){
                    end_time = to_string(h_end_index)+"0"+to_string(m_end_index);
                } else{
                    end_time = to_string(h_end_index)+to_string(m_end_index);
                }
            }
            cout << start_time << '-' << end_time << endl;
            start_index = -1;
        }
    }
    return 0;
}
