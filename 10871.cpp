#include <iostream>

int main() {
	int i, N, X, A;

	std::cin >> N >> X;
	for (i = 0; i < N; i++) {
		std::cin >> A;
		if (A < X)
			std::cout << A << " ";
	}

}