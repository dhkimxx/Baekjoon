#include <iostream>

int main() {
	int N, M, MAX = 0;
	std::cin >> N >> M;
	int* cards = new int[N];

	for (int i = 0; i < N; i++) {
		std::cin >> cards[i];
	}
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			for (int k = j + 1; k < N; k++) {
				if (cards[i] + cards[j] + cards[k] <= M) {
					if (cards[i] + cards[j] + cards[k] > MAX) {
						MAX = cards[i] + cards[j] + cards[k];
					}
				}
			}
		}
	}
	std::cout << MAX;
	return 0;
}