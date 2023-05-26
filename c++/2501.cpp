#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

int main() {
    FastIO;
    int N;
    int K;
    int result = 0;
    int cnt = 0;
    cin >> N >> K;
    for(int i = 1; i <= N; i++){
        if(N % i == 0){
            cnt += 1;
            if(cnt == K) result = i;
        }
    }
    cout << result;
}
