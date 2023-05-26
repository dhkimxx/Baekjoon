#include <iostream>

int main() {
	int M, N;

	std::cin >> M >> N;
	if (M < 2)
		M = 2;
	int* arr = new int[N + 1];
	for (int i = 0; i < N + 1; i++) {
		arr[i] = 0;
	}

	for (int i = 2; i <= N; i++) {

		if (arr[i])
			continue;
		else {
			if(i >= M) std::cout << i << "\n";
			for (int j = 2; i * j <= N; j++) {
				arr[i * j] = 1;
			}
		}
	}
}