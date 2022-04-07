#include <iostream>
#include <algorithm>

int des(int a, int b) {
	return a > b;
}

int main() {
	int arr[10] = { 0 };
	int N, count = 0; std::cin >> N;
	for (int i = N; i > 0; i = i / 10, count++) {
		arr[count] = i % 10;
	}
	std::sort(arr, arr + 10, des);
	for (int i = 0; i < count; i++) {
		std::cout << arr[i];
	}
}