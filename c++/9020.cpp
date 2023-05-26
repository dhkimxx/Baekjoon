#include <iostream>

int main() {
	int testcase, n;

	std::cin >> testcase;

	for (int i = 1; i <= testcase; i++) {

		std::cin >> n;

		int* arr = new int[n + 1];
		for (int i = 0; i < n + 1; i++) {
			arr[i] = 0;
		}

		for (int i = 2; i <= n; i++) {
			if (arr[i])
				continue;
			else {
				for (int j = 2; i * j <= n; j++) {
					arr[i * j] = 1;
				}
			}
		}
		for (int i = 0; i <= n / 2; i++) {
			if (!(arr[n / 2 - i] + arr[n / 2 + i])) {
				std::cout << n / 2 - i << " " << n / 2 + i << "\n";
				break;
			}
		}

	}
}