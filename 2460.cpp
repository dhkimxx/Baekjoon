#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

int main() {
    FastIO;
    int cnt = 0;
    int result = 0;
    for(int i = 0; i < 10; i++){
        int up, down;
        cin >> down >> up;
        cnt = cnt - down + up;
        result = max(result, cnt);
    }
    cout << result;
}
