#include <iostream>

int main() {
	int testcase, result, sum;
	int k, n;

	std::cin >> testcase;

	for (int t = 1; t <= testcase; t++) {
		std::cin >> k >> n;

		int *arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = i + 1;
		}

		for (int j = 0; j < k; j++) {

			sum = 0;
			for (int i = 0; i < n; i++) {
				sum += arr[i];
				arr[i] = sum;
			}

		}
		std::cout << sum << "\n";
		delete[] arr;
	}

}