#include <iostream>

int main() {
	int testnum, a,b,i;

	std::cin >> testnum;
	for (i = 0; i < testnum; i++) {
		std::cin >> a >> b;
		std::cout << a + b << "\n";
	}
	return 0;
}