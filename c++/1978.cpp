#include <iostream>

int main() {
	int testcase;
	int n, count;

	std::cin >> testcase;
	count = testcase;
	for (int i = 1; i <= testcase; i++) {
		std::cin >> n;
		if (n == 1)
			count--;
		else {
			for (int j = 2; j < n; j++) {
				if ((n / j) * j == n) {
					count--;
					break;
				}
			}
		}
	}
	std::cout << count;
	return 0;
}