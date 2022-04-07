#include <iostream>
using namespace std;

long long P[101] = {0, 1, 1, 1, 2};

long long count(int n) {
	if (!P[n] && n != 0)
		P[n] = count(n - 1) + count(n - 5);	
	return P[n];
}
int main() {
	int N; cin >> N;
	for (int i = 0; i < N; i++) {
		int temp; cin >> temp;
		if (temp <= 4) cout << P[temp] << "\n";
		else cout << count(temp) << "\n";
	}
}