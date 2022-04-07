#include <iostream>

int main() {
	int input, N;

	std::cin >> input;
	if (input == 1)
		return 0;
	N = input;
	for (int i = 2; i < N;) {
		if ((N / i) * i == N) {
			std::cout << i << "\n";
			N = N / i;
		}
		else
			i++;
	}
	
	std::cout << N;
	
}