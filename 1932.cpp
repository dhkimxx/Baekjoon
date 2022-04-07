#include <iostream>
using namespace std;

int max(int a, int b) {
	return(a > b ? a : b);
}

int main() {
	int N; cin >> N;
	int arr[500][500];
	int result = 0;
	for (int i = 0, j = 0; i < N; i++) {
		for (j = 0; j < i + 1; j++) {
			cin >> arr[i][j];
			if (j != 0 && j != i) {
				arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j]);
			}
		}
		if (i != 0) {
			arr[i][0] += arr[i - 1][0];
			arr[i][i] += arr[i - 1][i - 1];			
		}
	}
	for (int i = 0; i < N; i++) {
		result = max(arr[N - 1][i], result);
	}
	cout << result;
}