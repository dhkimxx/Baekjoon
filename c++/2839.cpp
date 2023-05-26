#include <iostream>

int main() {
	int N;

	int n3, n5;

	std::cin >> N;
	n5 = N / 5;
	n3 = N / 3;

	
	for (int i = n5; i >= 0; i--) {
		for (int j = 0; j <= n3; j++) {
			if (5 * i + 3 * j == N) {
				std::cout << i + j;
				return 0;
			}
		}
	}
	std::cout << -1;
}