#include <iostream>

int main() {
	int n, sum;
	char num;
	std::cin >> n;
	sum = 0;
	for (int i = 0; i < n; i++) {
		std::cin >> num;
		sum += (int)num - 48;
	}
	std::cout << sum;
	return 0;
}