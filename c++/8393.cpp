#include <iostream>

int main() {
	int n, sum = 0,i;

	std::cin >> n;
	for (i = 1; i <= n; i++) {
		sum += i;
	}
	std::cout << sum;
	return 0;
}