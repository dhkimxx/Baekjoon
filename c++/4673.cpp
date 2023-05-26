#include <iostream>

int arr[10001];

int d(int n) {
	int result = n;

	while (1) {
		if (n == 0) break;
		result += n % 10;
		n = n / 10;
	}
	return result;
}

int main() {
	for (int i = 1; i <= 10000; i++) {
		arr[d(i)] = true;
	}

	for (int i = 1; i <= 10000; i++) {
		if (arr[i] == false) {
			std::cout << i << "\n";
		}
	}
}