#include <iostream>

int main() {
	int n, count;

	while (1) {
		std::cin >> n;
		if (!n)
			break;

		int* arr = new int[2 * n + 1];
		for (int i = 0; i < 2 * n + 1; i++) {
			arr[i] = 0;
		}

		count = 0;
		for (int i = 2; i <= 2 * n; i++) {

			if (arr[i])
				continue;
			else {
				if (i > n) count++;
				for (int j = 2; i * j <= 2 * n; j++) {
					arr[i * j] = 1;
				}
			}
		}
		std::cout << count << "\n";
	}
}