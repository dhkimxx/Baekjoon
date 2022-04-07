#include <iostream>

int main() {
	int N; std::cin >> N;
	int* rank = new int[N];
	int** body = new int* [N];
	for (int i = 0; i < N; i++) {
		body[i] = new int[2];
		rank[i] = 1;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 2; j++) {
			std::cin >> body[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			if (i == k) {
				continue;
			}
			if (body[i][0] < body[k][0] && body[i][1] < body[k][1]) {
				rank[i]++;
			}		
		}
		std::cout << rank[i] << " ";
	}
}