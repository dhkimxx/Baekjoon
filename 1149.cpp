#include <iostream>
using namespace std;

int min(int a, int b) {
	return(a < b ? a : b);
}

int main() {
	int N; cin >> N;
	int weight[3][1000];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> weight[j][i];
		}
		if (i == 0)continue;
		weight[0][i] += min(weight[1][i - 1], weight[2][i - 1]);
		weight[1][i] += min(weight[0][i - 1], weight[2][i - 1]);
		weight[2][i] += min(weight[1][i - 1], weight[0][i - 1]);
	}
	cout << min(min(weight[0][N - 1], weight[1][N - 1]), weight[2][N - 1]);
}