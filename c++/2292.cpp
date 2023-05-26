#include <iostream>

int main() {
	int n, count = 1 ,s = 1;
	std::cin >> n;

	while (1) {
		if (n > s) {
			s += 6*count;
			count++;
		}
		else {
			std::cout << count;
			return 0;
		}
	}
}