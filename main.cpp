#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

bool visited[200001];
int dp[200001];
vector<int> vec;
int N;
int cnt;

int nextVertex(int n){
    int sum = n;
    while(n != 0){
        sum += n % 10;
        n = n / 10;
    }
    if(sum > N) sum -= N;
    return sum;
}

int dfs(int v){
    if(dp[v]){
        int cicleSize = dp[v];
        while (size(vec)){
            dp[vec.back()] = ++cicleSize;
            vec.pop_back();
        }
        return 0;
    }
    if(visited[v]){
        vector<int> cicle;
        int cicleSize = 0;
        while(size(vec)){
            cicleSize += 1;
            cicle.push_back(vec.back());
            vec.pop_back();
            if(cicle.back() == v) break;
        }
        for(int i: cicle){
            dp[i] = cicleSize;
        }
        while (size(vec)){
            dp[vec.back()] = ++cicleSize;
            vec.pop_back();
        }
        return 0;
    }
    visited[v] = true;
    cnt++;
    vec.push_back(v);
    return dfs(nextVertex(v));
}

int main() {
    FastIO;
    int result = 0;
    cin >> N;
    for(int i = 1; i <= N; i++){
        if(visited[i]) continue;
        vec.clear();
        cnt = 0;
        dfs(i);
        result = result > dp[i] ? result : dp[i];
    }
    cout << result;
}
