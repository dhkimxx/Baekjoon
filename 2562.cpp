#include <iostream>

int main() {
	int num = 9;
	int *arr = new int[num];
	int i, max = 0, max_id;

	for (i = 0; i < num; i++) {
		std::cin >> arr[i];
		if (arr[i] > max) {
			max = arr[i];
			max_id = i + 1;
		}

	}
	std::cout << max << "\n" << max_id;
	return 0;
	delete[] arr;
}