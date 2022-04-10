#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

bool visited[200001];
int dp[200001];
vector<int> vec;
int N;

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
        return dp[v];
    }
    else if(visited[v]){
        vector<int> cicle;
        int cicleSize = 0;
        while(true){
            cicleSize += 1;
            cicle.push_back(vec.back());
            vec.pop_back();
            if(cicle.back() == v) break;
        }
        for(int i: cicle){
            dp[i] = cicleSize;
        }
        return dp[v];
    }
    visited[v] = true;
    vec.push_back(v);
    int temp = dfs(nextVertex(v));
    if(dp[v] == 0) dp[v] = temp + 1;
    return dp[v];
}

int main() {
    FastIO;
    int result = 0;
    cin >> N;
    for(int i = 1; i <= N; i++){
        if(visited[i]) continue;
        vec.clear();
        dfs(i);
        result = result > dp[i] ? result : dp[i];
    }
    cout << result;
}
