#include <iostream>

int main() {
	int M, N, min, prime, sum = 0;

	std::cin >> M >> N;
	min = N;
	for (int i = M; i <= N; i++) {
		
		prime = i;

		if (i == 1)
			prime = 0;

		for (int j = 2; j < i; j++) {
			if ((i / j) * j == i) {
				prime = 0;
				break;
			}
		}
		sum += prime;

		if (prime) {
			if (prime < min) {
				min = prime;
			}
		}
	}
	if (sum)
		std::cout << sum << "\n" << min;
	else
		std::cout << -1;
}