#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int main() {
	int N, temp; std::cin >> N;
	int count[10001] = { 0, };
	for (int i = 0; i < N; i++) {
		scanf("%d", &temp);
		count[temp]++;
	}
	for (int i = 1; i < sizeof(count)/4; i++) {
		for (int j = 0; j < count[i]; j++) {
			std::cout << i << "\n";
		}
	}
}
