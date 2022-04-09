#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

int nextVertex[20001] = {0};
int dp[20001] = {0};
int visited[20001] = {0};
vector<int> Stack;
int Count = 0;

int numSum(int n){
    int numberSum = 0;
    while(n != 0){
        numberSum += n % 10;
        n = n / 10;
    }
    return numberSum;
}

int dfs(int v){
    if(visited[v]) return
    visited[v] = true;
    Stack.push_back(v);
    Count +=1;
    if(nextVertex[v] != 0){
        Count += dp[nextVertex[v]];
        return 0;
    }
    dfs(nextVertex[v]);
    return 0;
}

int main() {
    FastIO;
    int N;
    int result = 0;
    cin >> N;
    cout << N;
    for(int i = 1; i <= N + 1; i++){
        nextVertex[i] = i + numSum(i);
        if(nextVertex[i] > N){
            nextVertex[i] -= N;
        }

    }

    for(int i = 0; i <= N + 1; i++){
        if(dp[i] != 0) continue;
        *visited = {0};
        Stack.clear();
        Count = 0;
        dfs(i);
        dp[i] = Count;
        result = result > Count ? result : Count;
        for(int l = 1; l <= size(Stack) - 1; l++){
            dp[Stack[l]] = Count - 1;
        }

    }


    cout << result;
}
