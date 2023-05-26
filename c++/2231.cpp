#include <iostream>

int main() {
	int N; 
	std::cin >> N;
	for (int i = 1; i <= N; i++) {
		int j = i, sum = i;
		while (1) {
			sum += j % 10;

			if ((j / 10) == 0)
				break;
			else
				j = j / 10;
		}
		if (sum == N)
		{
			std::cout << i;
			break;
		}
		if (i == N) {
			std::cout << 0;
			break;
		}
	}
	return 0;
}