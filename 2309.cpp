#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;
vector<int> v;

int combination(int index, vector<int> temp_v){
    if(100 == accumulate(temp_v.begin(), temp_v.end(), 0)){
        if(7 == size(temp_v)){
            for(int i: temp_v){
                cout << i << '\n';
            }
            exit(0);
        }
    }
    if(index == 9)
        return 0;
    combination(index + 1, temp_v);
    temp_v.push_back(v[index]);
    combination(index + 1, temp_v);
    return 0;
}

int main() {
    FastIO;
    for(int i = 0; i < 9; i++){
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());
    vector<int> temp_v;
    combination(0, temp_v);
}
