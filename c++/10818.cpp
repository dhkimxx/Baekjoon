#include <iostream>

int main() {
	int num, max = -1000000, min = 1000000;
	int i;
	std::cin >> num;
	int* array = new int[num];

	for (i = 0; i < num; i++) {
		std::cin >> array[i];
		
		if (array[i] > max)
			max = array[i];
		if (array[i] < min)
			min = array[i];
	}
	std::cout << min << " " << max;
	delete[] array;
	return 0;
}