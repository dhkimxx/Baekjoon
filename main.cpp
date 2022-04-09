#include <bits/stdc++.h>
#define FastIO ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
using namespace std;

bool visited[200000];
int Count;
int N;

int numSum(int n){
    int numberSum = 0;
    while(n != 0){
        numberSum += n % 10;
        n = n / 10;
    }
    return numberSum;
}

int dfs(int v){
    int nextVertex;
    if(visited[v]) return 0;
    visited[v] = true;
    Count += 1;
    nextVertex = v + numSum(v);
    if(nextVertex > N) nextVertex -= N;
    return dfs(nextVertex);
}

int main() {
    FastIO;
    int result = 0;
    cin >> N;
    for(int i = 1; i <= N; i++){
        for(int n = 1; n <= N; n++) visited[n] = false;
        Count = 0;
        dfs(i);
        result = result > Count ? result : Count;
    }
    cout << result;
}
