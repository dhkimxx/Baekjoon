#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

int main() {
    FastIO;
    int T; cin >> T;
    int N;
    for(int i = 1; i  <= T; i++){
        cin >> N;
        int n = 0;
        while(N > 0){
            if(N % 2) cout << n << ' ';
            N /= 2;
            n++;
        }
        cout << '\n';
    }
}
