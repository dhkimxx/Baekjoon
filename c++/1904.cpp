#include <iostream>
using namespace std;

int main() {
	int N; cin >> N;
	int* arr = new int[N + 2];
	arr[1] = 1;
	arr[2] = 2;
	if (N <= 2) {
		cout << arr[N];
		return 0;
	}
	else {
		for (int i = 3; i <= N; i++){
			arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
		}
		cout << arr[N];
		return 0;
	}
}